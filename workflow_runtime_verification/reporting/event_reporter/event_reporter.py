import sys

from workflow_runtime_verification.reporting.event.checkpoint_reached_event import (
    CheckpointReachedEvent,
)
from workflow_runtime_verification.reporting.event.component_event import ComponentEvent
from workflow_runtime_verification.reporting.event.declare_variable_event import (
    DeclareVariableEvent,
)
from workflow_runtime_verification.reporting.event.task_finished_event import (
    TaskFinishedEvent,
)
from workflow_runtime_verification.reporting.event.task_started_event import (
    TaskStartedEvent,
)
from workflow_runtime_verification.reporting.event.variable_value_assigned_event import (
    VariableValueAssignedEvent,
)


class EventReporter:
    def __init__(self):
        self._output = sys.stdout

    # initialize: to file, to std out?
    def report_task_started(self, task_name, time):
        serialized_event = TaskStartedEvent(task_name, time).serialized()
        self._write(serialized_event)
        return serialized_event

    def report_task_finished(self, task_name, time):
        serialized_event = TaskFinishedEvent(task_name, time).serialized()
        self._write(serialized_event)
        return serialized_event

    def report_declared_variable(self, variable_name, variable_type, time):
        serialized_event = DeclareVariableEvent(
            variable_name, variable_type, time
        ).serialized()
        self._write(serialized_event)
        return serialized_event

    def report_checkpoint_reached(self, checkpoint_name, time):
        serialized_event = CheckpointReachedEvent(checkpoint_name, time).serialized()
        self._write(serialized_event)
        return serialized_event

    def report_variable_value_assigned(self, variable_name, variable_value, time):
        serialized_event = VariableValueAssignedEvent(
            variable_name, variable_value, time
        ).serialized()
        self._write(serialized_event)
        return serialized_event

    def report_component_event(self, component_name, data, time):
        serialized_event = ComponentEvent(component_name, data, time).serialized()
        self._write(serialized_event)
        return serialized_event

    def _write(self, serialized_event):
        self._output.write(serialized_event)
