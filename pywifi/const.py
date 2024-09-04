#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Constants used in pywifi library define here."""

# Define interface status.
IFACE_DISCONNECTED = 0
IFACE_SCANNING = 1
IFACE_INACTIVE = 2
IFACE_CONNECTING = 3
IFACE_CONNECTED = 4

# Define auth algorithms.
AUTH_ALG_OPEN = 1
AUTH_ALG_SHARED = 2

# Define auth key mgmt types.
AKM_TYPE_NONE = 0
AKM_TYPE_OPEN = 1
AKM_TYPE_SHARED = 2
AKM_TYPE_WPA = 3
AKM_TYPE_WPAPSK = 4
AKM_TYPE_WPANONE = 5
AKM_TYPE_WPA2 = 6
AKM_TYPE_WPA2PSK = 7
AKM_TYPE_WPA3 = 8
AKM_TYPE_WPA3SAE = 9
AKM_TYPE_OWE = 10
AKM_TYPE_WPA3ENT = 11

# Define ciphers.
CIPHER_TYPE_NONE = 0
CIPHER_TYPE_WEP = 1
CIPHER_TYPE_TKIP = 2
CIPHER_TYPE_CCMP = 4
CIPHER_TYPE_UNKNOWN = 5

KEY_TYPE_NETWORKKEY = 0
KEY_TYPE_PASSPHRASE = 1
