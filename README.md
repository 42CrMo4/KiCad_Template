# Diff conditions
Kibot.yml  
* add diff to last change
* Add diff to last tag/RC tag/both

Workflow
* Add condition if last tag is available in workflow
* Adapt all workflows accordingly 
  * Generate output
    * Last change
    * Last tag or RC tag
  * RC release
    * Last tag
    * Last rc tag
  * Release 
    * Last tag

# KiCad_Template

This is a template repo for KiCAD v6 projects with 

## Todo

* ~add DRC, ERC as seperate WF~ 
* ~add DRC, ERC to release WF as blocking~
* ~add release checklist~
* order release checklist
* ~add workflow to automatically create new realease checklist and realease note file and reset the generic for the next release~
* ~Rename artefacts with project name and date?~
* Add diffrent PCB manufactures output via kibot
* ~Update to kicad6_auto:1.3.0~
* use version number for template

## Usage

setting -> action -> general -> Workflow permissions -> Read and write permissions

## Description. 

|     Font      |     Back      |
| ------------- | ------------- |
|![PCB Top design](Fabrication/PCBdraw_Top.png)|![PCB Back design](Fabrication/PCBdraw_Back.png)|
