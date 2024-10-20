import FreeSimpleGUI as sg


# label = sg.Text("Convertor")
feet_label = sg.Text("Enter feet:    ")
input_feet = sg.InputText(tooltip="Enter the feet", size=(40, 1), key="feet")
inches_label = sg.Text("Enter inches:")
input_inches = sg.InputText(tooltip="Enter the inches", size=(40, 1), key="inches")
convert_button = sg.Button("Convert")

output_label = sg.Text(key="output", text_color="white")

window = sg.Window("Convertor", text_justification="center", titlebar_text_color="red",
                   layout=[
                           [feet_label, input_feet],
                           [inches_label, input_inches],
                           [convert_button, output_label]])

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Convert":
        feet = values["feet"]
        inches = values["inches"]
        feet = int(feet) if feet else 0
        inches = int(inches) if inches else 0
        total_inches = feet * 12 + inches
        meters = total_inches * 0.0254
        window["output"].update(f"{total_inches} inches is equal to {meters} meters.")

print("Goodbye!")

window.close()
