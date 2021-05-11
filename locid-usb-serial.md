# LOC.id USB Serial Protocol

## Host support
### Linux

The LOC.id-usb-module is supported out of the box on most distributions using the [usb cdc acm gadget](https://developer.ridgerun.com/wiki/index.php/How_to_use_USB_CDC_ACM_and_MS_composite_Linux_gadget_driver) driver.

When plugging in, a device node is spawned at `/dev/ttyACM*` which can be used for serial communication using regular tty emulation / file IO.

### Mac OS

USB cdc acm support is available out of the box from MacOS 10.9 onwards.

When plugging in, a device node is spawned at `/dev/tty.usbmodem0000000000001` which can be used for serial communication using regular tty emulation / file IO.

### Windows 10

USB cdc acm support is available out of the box from Windows 10 onwards.

When plugging in, windows spawns a virtual usb serial COM-Port device.

## Protocol

The serial protocol is based on newline(0x0A) separated [JSON-RPC 2.0](https://www.jsonrpc.org/specification) messages.

### Notifications

#### locid.status

Regular sent status information about connected users & proximity ranges.

**Example Payload (prettified)**
```javascript
{
  'method': 'locid.status',
  'params': {
    'users': [
        {'id': '0D028DA9906C', 'prox': 2},
        {'id': '0D028DC1008B', 'prox': 1}
      ]
  }
}
```

**Params**

|  Name       |  Type |  Description |
|:------------|:--------------------|:--------------------|
| users | array | Array of connected user objects. <br /><br/>id: unique user id<br/><br/>prox: Promity class<br />  1 - Nearby<br />  2 - Far <br />  0 - Out of range |

### Requests
tbd


