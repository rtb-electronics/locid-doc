# RTB Acoustic Guide Device Bluetooth GATT Service

## 1 Introduction

RTB acoustic guide devices implement a service according to the [Bluetooth Low Energy Generic Attribute Profile (GATT) 5.1](https://www.bluetooth.com/specifications/specs/core-specification-5-1/).

## 2 Service Declaration

The Service-UUID is:

        B940D010-F5F8-466E-AFF9-25556B57FE6D
        
## 3 Service Characteristics

| Characteristic             | Ref. | Requirement  |
|:---------------------------:|:-----:|:--------------------:|
| Version                    | [3.1](#31-version) | Mandatory|
| MAC                        | [3.2](#32-mac) | Mandatory|
| Enable                     | [3.3](#33-enable) | Mandatory|
| Near threshold             | [3.4](#34-near-threshold) | Mandatory|
| Far threshold              | [3.5](#35-far-threshold) | Mandatory|
| Longitude                  | [3.6](#36-longitude) | Optional|
| Latitude                   | [3.7](#37-latitude)  | Optional|
| Door                       | [3.8](#38-door)  | Optional|
| Vehicle name               | [3.9](#39-vehicle-name) | Optional |
| Traffic light request      | [3.10](#310-traffic-light-request) | Optional |

### 3.1 Version

| Name        | Version                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>0011</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Reads the firmware version.                 |
| Type        | string                              |
| Characteristic Properties | Read |

Read returns the firmware version of the device

### 3.2 MAC

| Name        | MAC                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D014</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Reads the mac address                    |
| Type        | 6 byte                                      |
| Characteristic Properties | Read |

Read returns the bluetooth mac address of the device

### 3.3 Enable

| Name        | Enable                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D016</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Enables the acoustic sound output.          |
| Type        | uint32                                       |
| Characteristic Properties        | Write, Write without response |

Enables/requests sound output of the acoustic guide device. The following activation modes are supported:

| Mode | Value |
|:-----|:----------|
| Far (ususally outputs a pilot / acoustic guide tone) | 2 |
| Near (ususally outputs a voice message or issues a button press on traffic lights) | 1 |
| Off / out of range | 0 |

### 3.4 Near threshold

| Name        | Near threshold                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D012</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Reads the near distance threshold.          |
| Type        | float32                                       |
| Characteristic Properties | Read |

Reads the distance (in m) the device considers a person to be in near range.

### 3.5 Far threshold

| Name        | Far threshold                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D013</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Reads the far distance threshold.          |
| Type        | float32                                       |
| Characteristic Properties | Read |

Reads the distance (in m) the device considers a person to be in far range.

### 3.6 Longitude

| Name        | Longitude                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D017</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Reads the geographic longitude   .          |
| Type        | float32                                       |
| Characteristic Properties | Read |

Reads the geographic longitude of the device.

### 3.7 Latitude

| Name        | Latitude                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D018</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Reads the geographic latitude.              |
| Type        | float32                                       |
| Characteristic Properties | Read |

Reads the geographic latitude of the device.

### 3.8 Door

| Name        | Door                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D019</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Reads the vehicle door state.              |
| Type        | uint8                                       |
| Characteristic Properties | Read, Notify |

Reads the door state. Used in public transport vehicles (trains/buses).

| Mode | Value |
|:-----|:----------|
| Door is open | 1 |
| Door is closed | 0 |

### 3.10 Traffic light request

| Name        | Door                                  |
|:------------|:--------------------------------------------|
| UUID        | B940<b>D024</b>-F5F8-466E-AFF9-25556B57FE6D |
| Description | Sends a request to cross the street.                       |
| Type        | None                                       |
| Characteristic Properties | Read, Notify |

Sends an assistive pedestrian request to cross the street.
