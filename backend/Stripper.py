import bluetooth
from strips.strip_utils import LedStripManager

test_strip_config = {
    "strips" : [
        {
            "name" : "Esstisch",
            "id": 0,
            "mode" : {
                "mode_id" : 1,
                "mode_color_h" : 255,
                "mode_color_s" : 0,
                "mode_color_v" : 255
            },
            "mac_address" : "98:D3:31:FD:89:CA"
        }
    ]
}
    
print("Init LED strip manager")
strip_manager = LedStripManager(test_strip_config)
print("Starting LED strip manager")

print("Diconnecting devices...")

