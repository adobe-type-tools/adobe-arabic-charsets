"""
Standards Mappings Auto-Loader

This module provides automatic discovery and loading of romanization standard
data files. Each data file contains METADATA and MAPPINGS for a specific standard.

Author: Adobe Arabic Charset Tools
Created: 2025-01-14
"""

import importlib
from pathlib import Path
from typing import Dict, Any, Optional


def derive_standard_name(metadata: Dict[str, Any]) -> str:
    """
    Derive standard name from metadata fields.
    
    Uses table_column + (language or table_type) to generate consistent naming.
    Special handling for extended table where column names are already fully qualified.
    
    Args:
        metadata: Metadata dictionary containing table_column, table_type, and optional language
        
    Returns:
        Derived standard name (e.g., 'BGN/PCGN Arabic', 'ALA-LC Pashto', 'CLE IPA')
    """
    table_column = metadata.get('table_column', '')
    language = metadata.get('language', '')
    table_type = metadata.get('table_type', 'arabic')
    
    # Special case: Extended table columns are already fully qualified
    # (e.g., "ALA-LC Pashto", "BGN/PCGN Baluchi")
    if table_type == 'extended':
        return table_column
    
    # Priority: language field takes precedence over table_type
    if language:
        return f"{table_column} {language}"
    else:
        # Handle both string and list table_type
        if isinstance(table_type, list):
            type_str = '/'.join([t.title() for t in table_type])
        else:
            type_str = table_type.title()
        return f"{table_column} {type_str}"


def load_all_standards() -> Dict[str, Dict[str, Any]]:
    """
    Auto-discover and load all standard data files in this directory.
    
    Returns:
        Dictionary mapping standard_name → {metadata, mappings}
    """
    standards = {}
    mapping_dir = Path(__file__).parent
    
    for py_file in sorted(mapping_dir.glob('*.py')):
        # Skip __init__.py
        if py_file.stem == '__init__':
            continue
        
        try:
            # Import the module
            module = importlib.import_module(f'standards_mappings.{py_file.stem}')
            
            # Get metadata and mappings
            if hasattr(module, 'METADATA') and hasattr(module, 'MAPPINGS'):
                metadata = module.METADATA
                mappings = module.MAPPINGS
                
                # Use standard_name if provided (for edge cases), otherwise derive from metadata
                standard_name = metadata.get('standard_name') or derive_standard_name(metadata)
                standards[standard_name] = {
                    'metadata': metadata,
                    'mappings': mappings,
                    'module_name': py_file.stem
                }
        except Exception as e:
            print(f"⚠️  Warning: Could not load {py_file.name}: {e}")
    
    return standards


def get_standard_mappings(standard_name: str) -> Optional[Dict[str, str]]:
    """
    Get romanization mappings for a specific standard.
    
    Args:
        standard_name: Name of the standard (e.g., 'BGN/PCGN Urdu')
        
    Returns:
        Dictionary mapping unicode_code → romanization, or None if not found
    """
    if standard_name not in ALL_STANDARDS:
        return None
    
    data = ALL_STANDARDS[standard_name]
    
    # Convert from {char: (unicode, rom)} to {unicode: rom}
    result = {}
    for char, (unicode_code, rom) in data['mappings'].items():
        result[unicode_code.upper()] = rom
    
    return result


def get_metadata(standard_name: str) -> Optional[Dict[str, Any]]:
    """
    Get metadata for a specific standard.
    
    Args:
        standard_name: Name of the standard (e.g., 'BGN/PCGN Urdu')
        
    Returns:
        Metadata dictionary, or None if not found
    """
    if standard_name not in ALL_STANDARDS:
        return None
    
    return ALL_STANDARDS[standard_name]['metadata']


def get_standards_by_table(table_type: str) -> list:
    """
    Get all standards for a specific table type.
    
    Args:
        table_type: Table type (e.g., 'urdu', 'persian', 'arabic')
        
    Returns:
        List of standard names for that table type
    """
    result = []
    for name, data in ALL_STANDARDS.items():
        if data['metadata'].get('table_type', '').lower() == table_type.lower():
            result.append(name)
    return sorted(result)


def get_all_table_types() -> list:
    """Return list of all table types"""
    table_types = set()
    for data in ALL_STANDARDS.values():
        table_type = data['metadata'].get('table_type')
        if table_type:
            table_types.add(table_type.lower())
    return sorted(table_types)


def list_available_standards() -> list:
    """Return list of all available standard names"""
    return sorted(ALL_STANDARDS.keys())


def get_unicode_values_from_standard(standard_module: str) -> set:
    """
    Extract all Unicode values from a standard mapping module.
    
    Args:
        standard_module: Module name (e.g., 'wp_saraiki_ipa')
    
    Returns:
        Set of Unicode hex codes (uppercase)
    
    Raises:
        ValueError: If module doesn't exist or has no MAPPINGS
    """
    try:
        module = importlib.import_module(f'standards_mappings.{standard_module}')
    except ModuleNotFoundError:
        raise ValueError(f"Module '{standard_module}' not found in standards_mappings/")
    
    if not hasattr(module, 'MAPPINGS'):
        raise ValueError(f"Module '{standard_module}' has no MAPPINGS attribute")
    
    # MAPPINGS format: {char: (unicode, romanization)}
    unicode_values = set()
    for char, (uni, rom) in module.MAPPINGS.items():
        unicode_values.add(uni.upper())
    
    return unicode_values


# Load all standards on import for easy access
ALL_STANDARDS = load_all_standards()

