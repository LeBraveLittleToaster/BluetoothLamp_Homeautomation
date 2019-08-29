def check_if_mode_is_valid(mode):
    return True


class LedStripManager:
    def __init__(self, strips):
        self.strips = strips

    def merge_strips(self, strips):
        self.strips = strips
        return True

    def get_all_strips(self):
        return self.strips