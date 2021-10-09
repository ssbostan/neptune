import pytest

@pytest.mark.run(order=3)
def test_app_cli_test(runner):
    result = runner.invoke(args=["app", "test"])
    assert result.exit_code == 0
