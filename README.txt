README File
GitHub Link: https://github.com/VincentL03/Assignment-10.1
Vincent Liu
CSE-20-03
ASSIGNMENT 10.1
Due 12/3/21

Description of class:
This program uses class "Instant_Noodles", and creates objects using the Instant Noodle class.
It has these specific methods: get_timer, set-brand, get_brand, set_noodle type, get_noodle_type, set_flavor, get_flavor, how_to_cook, and microwave
All Data Variables are private. This means any changes will require different set methods.
It also has a class variable, self.__timer, which changes accordingly to type of noodle the user chooses. Udon will take 8 minutes, Soba will take 2, and Ramen will take 5
The class utilizes 3 get-set method pairs and a single get_timer method. Timer cannot be changed manually, therefore it will only have a get method.
The other two methods included in this program are how_to_cook and microwave. Both utilize data created in the initializer and in get-set methods. These should be called last, after any changes the user wishes. 

Description of data variables:
self.__timer - Holds the integer that is the minutes in which the noodles are to be cooked. Will change automatically according to what noodle type user wants. Cannot be changed manually, and can be returned via the get_timer() method.
self.__brand - Holds a string of the brand the user wants. Can be changed with set_brand() method and returned via get_brand() method.
self.__noodle_type - Holds a string of the noodle type that the user wants. Can be changed with set_noodle_type() method and returned via get_noodle_type() method.
self.__flavor - HOlds a string of the noodle flavor. Can be Can be changed with set_flavor() method and returned via get_flavor() method.


Description of what each method does:
get_timer() - Will return the integer which represents time in minutes of how long you should microwave your noodles
set_brand(x) - Will set a brand of instant noodles to a user's input if the input is one of the three valid inputs. The valid arguments are as follows: Maruchan, Nissin or Nongshim. Takes in one argument
get_brand() - Will return the name of the brand chosen by the user. DOES NOT PRINT
set_noodle_type(x) = Similar to the other set methods, this method will take in one argument, and if valid, will set to that noodle type. Valid noodle types includes: Udon, Soba, Ramen
get_noodle_type() - Will return a string of the name of noodle type chosen. DOES NOT PRINT
set_flavor(x) - Sets a flavor depending on whether user input argument is a valid option. Takes one argument. Valid flavors are: Chicken, Beef, Shrimp, Pork
get_flavor() - Will return the user's noodle flavor. DOES NOT PRINT
how_to_cook() - Will print instructions on how to cook the different types of noodles. What is printed will depend on what noodle is chosen by the user
microwave(x) - Requires an integer argument in to work. The argument should be the minutes to microwave. It is recommended that the user calls the instructions to find out how long to microwave. Will print an error message if time input is not correct for correlating noodle type.
		Prints a timer second by second until timer gets to zero. When countdown reaches 0, the program will print that it has been completed and "Enjoy your meal".


Demo program:
The demo program should only be done within the main() function, which can be found near the bottom of the program
Some methods will take arguments, some will not. Instructions in detail on how to use them is in the following parts.

Within the main() function you are able to call any of the valid functions that were described above in the method descriptions
All methods starting with set will require an argument within the parenthesis following the name. For example; set_flavor("Chicken"). Chicken in quotes is the argument.
For the methods that begin with set, be sure to include the quotation marks in the argument, as it is required that arguments are strings. All other forms of arguments will be invalid, such as float/integers.
All methods beginning with get will require a print statement. For example, to get_flavor, one must write this in the main function; print(get_flavor()). Get methods are unable to take in arguments, neither should they be taking arguments. We must print because the get methods only return values.

 How to set up demo program:
	Part 1 - Choosing your noodles
		Step 1: Create an object name of your choice and have it equal "Instant_Noodles()". Inside the parenthesis, there should be 3 string arguments in quotations marks, separated by commas, which will be in this order; Brand, Noodle Type, Flavor.
			keep in mind that valid options are limited and are listed below:
			Valid Brands:
				Nongshim, Nissin, Maruchan
			Valid Noodle Types:
				Udon, Ramen, Soba
			Valid Flavors:
				Chicken, Pork, Shrimp, Beef
			Here is an example object that is valid: mynoodle = Instant_Noodles("Nongshim", "ramen", "shrimp")
			Make sure there is an indentation before the name of your object name, so that it will work under the main() function
	Part 2 - Making Changes with set methods (optional):
		Part 2.1  - Make any changes to brand
				Step 1 - Type your object name followed by .set_brand(), no spaces. the area within the parenthesis should be a string in quotation marks of a valid brand you wish to change your current one to. Please ensure you choose a valid option, otherwise you will be given a default brand of "nissin"
		Part 2.2  - Make changes to noodle type
				Step 1 - Type your object name followed by .set_noodle_type(), no spaces. the area within the parenthesis will be a string in quotation marks of a valid noodle you wish to change your current one to. Please ensure you choose a valid option, otherwise you will be given a default type of "ramen"
		Part 3.3  - Make changes to flavor
				Step 1 - Type your object name followed by .set_flavor(), no spaces. the area within the parenthesis will be a string in quotation marks of a valid flavor you wish to change your current one to. Please ensure you choose a valid option, otherwise you will be given a default type of "shrimp"
	
	Part 3 - Finding out if your chosen options were valid
		Step 1 - Type print(), then within the parenthesis, type the name of your object, followed by any of the get methods listed above (.get_brand(), .get_noodle_type(), .get_flavor()). 
			The get methods will not take in any arguments. 
			Here is an example of what this step should look like: print(self.get_brand()) 
			**Note that "self" in the example should be the name of your object**

	Part 4 - Find instructions on how long you should microwave your noodles
		Type the name of your object, followed by .how_to_cook() to call the method. This will print instructions on how to cook the specified noodle you chose. It will also include how long you should microwave your noodles. You will need to remember this for the next function
		Example: self.how_to_cook(). Again, self should be replaced with your chosen object name
	
	Part 5 - Microwave your noodles
		This method will print a timer counting down in seconds it takes your noodles to cook in the microwave. Type your object name, then .microwave() to call the microwave method.
		**Note** This method takes in 1 argument, an integer. The integer should be the length of time in minutes you must cook your noodles. This information on how long you must cook the noodles can be found in the .how_to_cook() method
		Example: self.microwave(). Again, self should be replaced with your chosen object name
 
When attempting to run the demo program, it is recommended to run one print statement at a time, as reading the terminal/console can be confusing when trying to figure out what is being printed out.
If you typed out all the methods explained above into the main file, be sure to comment out some gets methods so you don't get overwhelmed with print outputs.

An example of what the test code should look like can be found at the bottom of the main() function. All are already commented out