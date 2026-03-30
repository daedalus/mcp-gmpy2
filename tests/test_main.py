"""Tests for mcp-gmpy2 __main__."""

from unittest.mock import patch

from mcp_gmpy2 import __main__


def test_main_function_exists():
    """Test that main function exists and is callable."""
    assert callable(__main__.main)


def test_main_returns_int():
    """Test that main returns an int."""
    assert __main__.main.__annotations__.get("return") is int


@patch("mcp_gmpy2.__main__.mcp")
def test_main_calls_mcp_run(mock_mcp: object) -> None:
    """Test that main calls mcp.run()."""
    mock_mcp.run.return_value = None
    result = __main__.main()
    mock_mcp.run.assert_called_once()
    assert result == 0
