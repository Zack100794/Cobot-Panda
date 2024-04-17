import pytest
from calc.Code_source import CobotSafetyMonitor

# Define fixtures for the CobotSafetyMonitor instance
@pytest.fixture
def safety_monitor():
    return CobotSafetyMonitor()

# Test case for monitoring environment
def test_monitor_environment(safety_monitor):
    safety_monitor.monitor_environment()  # Call the method
    # Assert that the method was called
    assert safety_monitor.monitor_environment_called

# Test case for monitoring proximity
def test_monitor_proximity(safety_monitor):
    safety_monitor.monitor_proximity()  # Call the method
    # Assert that the method was called
    assert safety_monitor.monitor_proximity_called

# Test case for monitoring force/torque
def test_monitor_force_torque(safety_monitor):
    safety_monitor.monitor_force_torque()  # Call the method
    # Assert that the method was called
    assert safety_monitor.monitor_force_torque_called

# Test case for monitoring vision
def test_monitor_vision(safety_monitor):
    safety_monitor.monitor_vision()  # Call the method
    # Assert that the method was called
    assert safety_monitor.monitor_vision_called

# Test case for emergency stop
def test_emergency_stop(safety_monitor):
    safety_monitor.emergency_stop()  # Call the method
    # Assert that the method was called
    assert safety_monitor.emergency_stop_called

# Test case for the run method
def test_run(safety_monitor):
    safety_monitor.run()  # Call the method
    # Assert that all monitoring methods were called
    assert safety_monitor.monitor_environment_called
    assert safety_monitor.monitor_proximity_called
    assert safety_monitor.monitor_force_torque_called
    assert safety_monitor.monitor_vision_called
    # Assert that the detect_collision method was called
    assert safety_monitor.detect_collision_called
    # Assert that the emergency_stop method was called if collision detected
    assert safety_monitor.emergency_stop_called == safety_monitor.detect_collision_result
