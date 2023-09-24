
#libraries needed to make calculator app
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

# Define the class for my function and name my main function
class CalApp(App):
    def build(self):
        self.icon = "cal1.png" #change icon
        self.keys =["/","*","-","+"] #instance keys 
        self.last_known_keys = None #variable
        self.last_button = None #variable

        main_layout = BoxLayout(orientation = "vertical") # creating main layout and include box layout inside of main layout
        self.solution = TextInput(background_color = "black", foreground_color = "white", 
                                  multiline=False, halign="right", font_size=60, readonly=True)

        main_layout.add_widget(self.solution)# adding screen inside mainlayout
        buttons =[
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","+"],
            [".","0","C","-"],
        ]

        for row in buttons:# for loop for the creating buttons
            h_layout = BoxLayout() # creating box for the buttons
            for label in row:
                button = Button( #styling for font text and color and placement of the button
                    text =  label, font_size=30, background_color="blue",
                    pos_hint={"center_x":0.5, "center_y":0.5},
                )
                button.bind(on_press=self.on_button_press) # function for button when press
                h_layout.add_widget(button) #adding buttons inside layout
            main_layout.add_widget(h_layout)

        equal_button = Button( # equal buttton and it style color and placement
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x":0.5, "center_y":0.5},
        ) 
        equal_button.bind(on_press=self.on_solution)#function for equal button and adding it inside of layout
        main_layout.add_widget(equal_button)

        return main_layout  # return
    
    #define on_button_press function / passing self and instance
    def on_button_press(self,instance):
        current = self.solution.text  # function everytime someone press button it will display in text
        button_text = instance.text

        #clear screen from enter
        if button_text == 'C':
            self.solution.text =""
               #add key or operator
        else:
            if current and (
                self.last_known_keys and button_text in self.keys):# if an key is press after another key is choose nothing will return
                return 
            elif current =="" and button_text in self.keys: #if empty can't type operator as first operator return none
                return
            else:
                new_text = current + button_text 
                self.solution.text = new_text # store value 
        self.last_button = button_text 
        self.last_known_keys = self.last_button in self.keys
    


    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
     
    
# Function to call the main function to run the app
if __name__ == "__main__":  
    app = CalApp() #calling the function
    app.run() # running the app



