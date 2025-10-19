import numpy as np

from workflow_runtime_verification.components.component import Component


class SimpleDisplay(Component):
    def write(self, data: np.uint16):
        pass

    def stop(self):
        pass

    def state(self):
        return {}

    def exported_functions(self):
        return {"display_write": self.write}
