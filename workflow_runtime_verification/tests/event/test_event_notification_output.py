import io
import sys

from workflow_runtime_verification.tests.test import Test


class EventNotificationOutputTest(Test):
    def test_outputs_event_to_standard_output(self):
        output_buffer = self._buffer_capturing_standard_output()
        event_reporter = self.objects.event_reporter()

        serialized_event = event_reporter.report_task_started(
            self.objects.task_name(), self.objects.time()
        )

        line_read_from_standard_output = self._read_last_line_from(output_buffer)
        self.assertEqual(serialized_event, line_read_from_standard_output)
        self._restore_standard_output()

    @staticmethod
    def _buffer_capturing_standard_output():
        buffer = io.StringIO()
        sys.stdout = buffer
        return buffer

    @staticmethod
    def _restore_standard_output():
        sys.stdout = sys.__stdout__

    @staticmethod
    def _read_last_line_from(output_buffer):
        lines = output_buffer.getvalue().splitlines()
        return lines[-1] if lines else None
