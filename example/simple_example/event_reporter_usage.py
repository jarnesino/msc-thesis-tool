import os
import shutil
import sys

from workflow_runtime_verification.reporting.event_reporter.event_reporter import (
    EventReporter,
)


class Clock:
    def __init__(self):
        self._count = 0

    def current(self):
        return self._tick()

    def _tick(self):
        self._count += 1
        return self._count


clock = Clock()

report_file_name = "main_log.txt"
with open(report_file_name, "w+") as report_file:
    event_reporter = EventReporter(report_file)

    event_reporter.report_declared_variable("fail_safe_lock", "bool", clock.current())
    event_reporter.report_variable_value_assigned(
        "fail_safe_lock", "False", clock.current()
    )

    event_reporter.report_declared_variable("stage", "int", clock.current())
    event_reporter.report_variable_value_assigned("stage", "1", clock.current())

    event_reporter.report_task_started(
        "initiate_pressure_measurements", clock.current()
    )
    event_reporter.report_checkpoint_reached("control_failsafe", clock.current())
    event_reporter.report_declared_variable("pressure", "int", clock.current())
    event_reporter.report_variable_value_assigned("pressure", "156", clock.current())
    event_reporter.report_component_event(
        "display", "display_write,156", clock.current()
    )
    event_reporter.report_task_finished(
        "initiate_pressure_measurements", clock.current()
    )
