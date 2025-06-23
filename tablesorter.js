// Modern Table Sorter
// Based on original work by Bob Swift and contributors
// 
// Copyright (c) 2005, 2012 Bob Swift and other contributors
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
//     * Redistributions of source code must retain the above copyright notice,
//       this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//     * The names of contributors may not be used to endorse or promote products
//       derived from this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
//
// Modified and enhanced 2025 - Complete rewrite using modern JavaScript
// Copyright (c) 2025. All rights reserved.

class TableSorter {
    constructor() {
        // Cache regex patterns
        this.NUMBER_PATTERN = /^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$/;
        this.UNICODE_PATTERN = /[\u0600-\u06FF]/;
        
        // Initialize value parsers with memoization
        this.parsers = {
            string: this.memoize(value => this.getElementText(value).trim().toUpperCase()),
            number: this.memoize(value => {
                const text = this.getElementText(value).replace(/[^\d.-]/g, '');
                return text ? parseFloat(text) : -Infinity;
            }),
            unicode: this.memoize(value => this.getElementText(value)),
            default: this.memoize(value => this.getElementText(value))
        };

        // Cache for column types
        this.columnTypeCache = new WeakMap();

        // Bind methods once
        this.handleSort = this.handleSort.bind(this);
        this.initializeTables = this.initializeTables.bind(this);

        // Initialize tables when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', this.initializeTables);
        } else {
            this.initializeTables();
        }
    }

    // Memoization helper
    memoize(fn) {
        const cache = new WeakMap();
        return function(value) {
            if (!value) return '';
            if (cache.has(value)) return cache.get(value);
            const result = fn(value);
            cache.set(value, result);
            return result;
        };
    }

    // Get text content from element, handling various browser implementations
    getElementText(element) {
        return element?.textContent || element?.innerText || '';
    }

    // Determine the type of data in a column
    detectColumnType(table, columnIndex) {
        // Check cache first
        const cacheKey = `${columnIndex}`;
        const cachedType = this.columnTypeCache.get(table)?.[cacheKey];
        if (cachedType) return cachedType;

        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody?.rows || []);
        
        // Check first few non-empty values
        const samples = rows
            .map(row => this.getElementText(row.cells[columnIndex]))
            .filter(text => text.trim())
            .slice(0, 5);

        let type = 'string';
        if (samples.length > 0) {
            if (samples.every(sample => this.NUMBER_PATTERN.test(sample.trim()))) {
                type = 'number';
            } else if (samples.some(sample => this.UNICODE_PATTERN.test(sample))) {
                type = 'unicode';
            }
        }

        // Cache the result
        if (!this.columnTypeCache.has(table)) {
            this.columnTypeCache.set(table, {});
        }
        this.columnTypeCache.get(table)[cacheKey] = type;
        
        return type;
    }

    // Compare two values based on type
    compareValues(a, b, type) {
        // Handle empty values - empty values always sort to bottom
        const isEmptyA = !a || a.trim() === '';
        const isEmptyB = !b || b.trim() === '';
        
        if (isEmptyA && isEmptyB) return 0;
        if (isEmptyA) return 1;  // Empty values always go to bottom
        if (isEmptyB) return -1; // Non-empty values always go to top
        
        // If neither is empty, compare based on type
        switch (type) {
            case 'number':
                return a - b;
            case 'unicode':
                return a.localeCompare(b, 'ar');
            default:
                return a.localeCompare(b);
        }
    }

    // Sort table data
    sortTableData(table, columnIndex, ascending) {
        const tbody = table.querySelector('tbody');
        if (!tbody) return;

        const rows = Array.from(tbody.rows);
        const type = this.detectColumnType(table, columnIndex);
        const parser = this.parsers[type] || this.parsers.default;

        // Pre-parse values for efficiency
        const rowsWithValues = rows.map(row => ({
            row,
            value: parser(row.cells[columnIndex])
        }));

        // Sort rows
        rowsWithValues.sort((a, b) => {
            const valueA = a.value;
            const valueB = b.value;
            
            // First check for empty values - these always sort to bottom regardless of direction
            const isEmptyA = !valueA || valueA.trim() === '';
            const isEmptyB = !valueB || valueB.trim() === '';
            
            if (isEmptyA && isEmptyB) return 0;
            if (isEmptyA) return 1;  // Empty values always go to bottom
            if (isEmptyB) return -1; // Non-empty values always go to top
            
            // If neither is empty, sort based on direction
            const result = this.compareValues(valueA, valueB, type);
            return ascending ? result : -result;
        });

        // Update DOM efficiently
        const fragment = document.createDocumentFragment();
        rowsWithValues.forEach(({row}) => fragment.appendChild(row));
        tbody.appendChild(fragment);
    }

    // Update sort indicators in table header
    updateSortIndicators(table, columnIndex, ascending) {
        const headers = table.querySelectorAll('th');
        headers.forEach(header => {
            header.removeAttribute('data-sort-direction');
            header.classList.remove('sort-asc', 'sort-desc');
        });

        const header = headers[columnIndex];
        if (header) {
            const direction = ascending ? 'asc' : 'desc';
            header.setAttribute('data-sort-direction', direction);
            header.classList.add(`sort-${direction}`);
        }
    }

    // Handle sort event
    handleSort(event) {
        const th = event.target.closest('th');
        if (!th) return;

        const table = th.closest('table');
        const headers = table.querySelectorAll('th');
        const columnIndex = Array.from(th.parentNode.children).indexOf(th);
        
        // Check if we're sorting a new column
        const isNewColumn = th.sortFirstTime;
        
        // Reset all other headers
        headers.forEach(header => {
            if (header !== th) {
                header.sortFirstTime = true;
                header.sortDescending = false;
            }
        });

        // If it's a new column, start with ascending
        if (isNewColumn) {
            th.sortDescending = false;
        } else {
            // Toggle direction for subsequent clicks on same column
            th.sortDescending = !th.sortDescending;
        }
        th.sortFirstTime = false;

        this.sortTableData(table, columnIndex, !th.sortDescending);
        this.updateSortIndicators(table, columnIndex, !th.sortDescending);
    }

    // Initialize sortable tables
    initializeTables() {
        const tables = document.querySelectorAll('.confluenceTable');
        
        tables.forEach(table => {
            // Add click event listener using event delegation
            table.addEventListener('click', this.handleSort);

            // Initialize sort indicators
            const headers = table.querySelectorAll('th');
            const fragment = document.createDocumentFragment();
            
            headers.forEach(header => {
                // Initialize sort state
                header.sortFirstTime = true;
                header.sortDescending = false;
                
                header.style.cursor = 'pointer';
                header.setAttribute('title', 'Click to sort');
                
                // Create sort indicator element
                const indicator = document.createElement('span');
                indicator.className = 'sort-indicator';
                indicator.setAttribute('aria-hidden', 'true');
                fragment.appendChild(indicator.cloneNode(true));
            });
            
            // Batch DOM updates
            headers.forEach((header, i) => header.appendChild(fragment.children[0]));
        });
    }
}

// Initialize table sorter
const tableSorter = new TableSorter(); 