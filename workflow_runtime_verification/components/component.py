class Component:
    def stop(self):
        raise NotImplementedError

    def state(self):
        raise NotImplementedError

    def process_high_level_call(self, call_data):
        raise NotImplementedError
