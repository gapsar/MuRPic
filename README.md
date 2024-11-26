# μRpic  

*Yet Another Modular Raspberry Pi Camera System*  

<img src="https://github.com/user-attachments/assets/0a3a916c-29d4-47e9-83fa-67adc9c05ab2" alt="Components" width="70%" /> 

## Overview  

**μRpic** is a modular camera system based on a Raspberry Pi, offering flexibility and customization for users. Using off-the-shelf components enclosed in a 3D-printed case, this project allows you to build a customizable camera for diverse applications.  

## Features  

- **Modular Design**: Easily adapt and extend hardware components.  
- **Custom Software**: Four customizable software windows:
  1. Main Preview: Overlay with battery and mode status.  
  2. Mode Selection: Switch between available modes.  
  3. Settings: Adjust parameters for the current mode.  
  4. Miscellaneous Info: Display mode-specific data.  
- **Compatibility**: Supports all original Raspberry Pi Camera Module PCBs and can be modified for others.  

## Modularity  

The 3D-printed case is designed for minimal support use and consists of four main parts:  

<table align="center">
  <tr>
    <td><strong>Part</strong></td>
    <td><strong>Description</strong></td>
  </tr>
  <tr>
    <td><strong>Back Case</strong></td>
    <td>The back of the case with buttons and screen.</td>
  </tr>
  <tr>
    <td><strong>Front Case</strong></td>
    <td>The front of the case with the battery compartment.</td>
  </tr>
  <tr>
    <td><strong>Camera Support</strong></td>
    <td>The camera support that glues to the front for easier printing experience.</td>
  </tr>
  <tr>
    <td><strong>Removable Adapter Plate</strong></td>
    <td>The removable adapter plate that can be changed on the fly with just two screws.</td>
  </tr>
</table>

<img src="https://github.com/user-attachments/assets/5045f166-d893-4fbe-971e-cdb5403ea8ab" alt="Exploded View" width="49%" />  
<img src="https://github.com/user-attachments/assets/7c344d2a-1364-4889-9ebf-31d9c86ef1f3" alt="Basic Case" width="49%" />  

## Components  

<table align="center">
  <tr>
    <td style="width: 50%; text-align: left;">
      <table align="left">
        <tr>
          <td><strong>Component</strong></td>
          <td><strong>Description</strong></td>
        </tr>
        <tr>
          <td><strong>Raspberry Pi 4</strong></td>
          <td>The brain of the system.</td>
        </tr>
        <tr>
          <td><strong>Waveshare 4.3" Touchscreen</strong></td>
          <td>Compact display for live interaction.</td>
        </tr>
        <tr>
          <td><strong>Homemade Battery Pack</strong></td>
          <td>3P battery pack using 18650 cells.</td>
        </tr>
        <tr>
          <td><strong>Arducam 64MP Autofocus</strong></td>
          <td>High-resolution camera module.</td>
        </tr>
      </table>
    </td>
    <td style="width: 50%; text-align: right;">
      <img src="https://github.com/user-attachments/assets/a4180adf-b295-4b8b-a197-ec2694c08276" alt="Components" width="100%" />
    </td>
  </tr>
</table>

## Life plan of the project

This is the first viable version of the camera and another one is already in preparation, with some improvements to the battery pack and overall design.
For some application, the addition of a few sensors is also in progress.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b490d087-e5e6-4c99-870d-383d8adb6c1e" alt="Components" width="50%" />
</p>

## Installation & Setup

*Coming Soon!*  
This section will include:  
1. **Hardware Assembly**: Step-by-step instructions with diagrams.  
2. **Software Setup**: Installing dependencies and configuring the system.  
3. **Customization Tips**: Modifying for specific use cases.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/8888a880-484f-4e36-bcb9-a7cf4610fcff" alt="Components" width="50%" />
</p>

## Contributing  

A significant portion of the code was cleaned and improved by local LLMs. If you’d like to add features or new modes, feel free to submit a pull request. Contributions are welcome!

## License  

μRpic is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.  
