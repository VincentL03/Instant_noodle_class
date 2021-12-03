#Vincent Liu
#Assignment 10.1

#This program is about a real life object, Instant noodles. The class takes in arguments for flavor, noodle type and brand. there are get-set methods for these arguments. there is a timer that changes according to the type of noodles
 
 #TA Sebastian Reyes helped me with this, approved of the other two methods that were non-trivial
 #said that the set-get methods should always return, and that the microwave() method should 

import time #we will use this for a timer


class Instant_Noodles:
  def __init__(self, brand = "nissin", noodle_type = "ramen", flavor = "chicken"):
    #sets private data attributes
    self.__timer = 5
    self.__brand = brand
    self.__noodle_type = noodle_type
    self.__flavor = flavor
    #ensures that the original inputs are valid, otherwise, set to original ramen
    lowered_brand = brand.lower()
    if lowered_brand == "nissin":
      self.__brand = brand
    elif lowered_brand == "nongshim":
      self.__brand = brand
    elif lowered_brand == "maruchan":
      self.__brand = brand
    else:
      print(f"Sorry, we couldn't find the '{brand}' brand, we'll give you 'Nissin' brand noodles.")
      self.__brand = "nissin"
    #ensures the validity of noodle flavors
    lowered = flavor.lower()
    if lowered == "chicken":
      self.__flavor = flavor
    elif lowered == "beef":
      self.__flavor = flavor
    elif lowered == "pork":
      self.__flavor = flavor
    else:
      self.__flavor = "shrimp"
  #sets the proper names of noodle type and correlating time it takes to cook
    lowered_noodle_type = noodle_type.lower()
    if lowered_noodle_type == "udon":
      self.__noodle_type = noodle_type
      self.__timer = 8
    elif lowered_noodle_type == "soba":
      self.__noodle_type = noodle_type
      self.__timer = 2
    else:
      self.__noodle_type = "ramen"
      self.__timer = 5
  
#######################################
#method to return the timer 
  def get_timer(self):
    return self.__timer

#######################################
#sets/changes brand name
  def set_brand(self, new_brand):
    lowered = new_brand.lower() #makes the input argument lowercase. if it is one of the following below, it will be left alone, however if it isn't it will be set nissin
    if lowered == "nissin": 
      self.__brand = new_brand
    elif lowered == "nongshim":
      self.__brand = new_brand
    elif lowered == "maruchan":
      self.__brand = new_brand
    else:
      self.__brand = "nissin"

#gets and returns brand name
  def get_brand(self):
    return self.__brand

#######################################
#changes the noodle type
  def set_noodle_type(self, new_type):
    lowered = new_type.lower()  #makes the input argument lowercase. if it is one of the following below, it will be left alone, however if it isn't it will be set to ramen
    if lowered == "udon":
      self.__noodle_type = new_type
      self.__timer = 8
    elif lowered == "soba":
      self.__noodle_type = new_type
      self.__timer = 6
    else:
      self.__noodle_type = "ramen"
      self.__timer = 5
    return self.__noodle_type

#######################################

  def get_noodle_type(self):
    return self.__noodle_type

#######################################

  def set_flavor(self, new_flavor):
    lowered = new_flavor.lower()
    if lowered == "chicken":
      self.__flavor = new_flavor
    elif lowered == "beef":
      self.__flavor = new_flavor
    elif lowered == "pork":
      self.__flavor = new_flavor
    else:
      self.__flavor = "shrimp"
    return self.__flavor

#######################################

  def get_flavor(self):
    return self.__flavor

#######################################  

  def how_to_cook(self):
    noodle_type = self.get_noodle_type()
    flavor = self.get_flavor()
    
    if noodle_type.lower() == "udon":
      print("---------------------------")
      print("We will cook these instant noodles via microwave")
      print("How to cook your noodle type: Udon")
      print(f"We begin by placing the noodle, soup base, {flavor} flavor and dried vegetables into a bowl")
      print("Fill bowl with 2 cups of water")
      print("Microwave the udon for 8 minutes")
      print("Stir noodles")
      print("Enjoy!")
      print("---------------------------")
    elif noodle_type.lower() == "soba":
      print("---------------------------")
      print("We will cook these instant noodles via microwave")
      print("How to cook your noodle type: Soba")
      print(f"We begin by placing the noodle, soup base, {flavor} flavor and dried goods into a bowl")
      print("Fill bowl with 2 cups of water")
      print("Microwave the udon for 2 minutes")
      print("Enjoy!")
      print("---------------------------")
    elif noodle_type.lower() == "ramen":
      print("---------------------------")
      print("We will cook these instant noodles via microwave")
      print("How to cook your noodle type: Ramen")
      print(f"We begin by placing the noodle, soup base, {flavor} and dried vegetables into a bowl")
      print("Microwave the udon for 5 minutes")
      print("Fill bowl with 2 cups of water")
      print("Stir noodles, then Enjoy!")
      print("---------------------------")
    else:
      print(f"Your noodle type {noodle_type} wasn't found. Unable to print instructions") #in case something fails and the user's noodle type is invalid, this will print

#######################################

  def microwave(self, m_time):
    brand = self.get_brand()
    noodle_type = self.get_noodle_type()
    flavor = self.get_flavor()

    if noodle_type == "udon":
      self.__timer = 8
    elif noodle_type == "soba":
      self.__timer = 2
    else:
      self.__noodle_type = "ramen"
      self.__timer = 5
    
    #Check if user input is correct for their noodle type
    if m_time == self.__timer:
      secs = m_time * 60
    else:
      print(f"Sorry, the time you input to microwave '{noodle_type}' is wrong. Please find the proper time to microwave via the how_to_cook() method")
      quit()
    
    print(f"Please wait for {secs} seconds as we microwave this")
    for i in range(secs):
      print(f"{secs - i} seconds left...")
      time.sleep(1)

    output = ("✫ • ° •　　　　　　 · 　 ✲ ✧ ☆ . • •　　　 ✩ ✧ ☆　　　• °　　✽ • ★ . · ✧ ☆ . · .　 ☆　∗ .☆ •" "\n"
      "★ °　　　　　　　✧ • ★ °　　　　　　　✧ . ✫ • ° •　　　　　　 · 　 ✲ ✧ ☆ °　" "\n"
      "✧ •　　　　　　 · 　 ✲ ✧ ☆ . • •　　　 ✩ ✧ ☆　　　• • • ★ . · ✧ ☆ . · .　 ☆　∗ .☆ • ★ °　" "\n"
      f"           You microwaved {brand} brand {noodle_type}, {flavor} flavor for {secs} seconds" "\n"
      "                                   Enjoy your meal!" "\n"
      "✧ ∗ . • ★ °　　　　　　　✧ . ✫ • ° •　　　　　　 · 　 ✲ ✧ ☆ . • •　　　 ✩ ✧ ☆　　　• °" "\n"
      "✽ • ★ . · ✧ ☆ . · .　 ☆　∗ .☆ • ★ °　　　　　　　✧ • ★ °　　　　　　　✧ . ✫ • ° •" "\n"
      "  · 　 ✲ ✧ ☆ °　　　　　　　✧ •　　　　　　 · 　 ✲ ✧ ☆ . • •　　　 ✩ ✧ ☆　　　•")
    print(output)
    return output

#######################################
###       MAIN Function    ############

def main():
  #insert your code here#













  '''
  #mynoodle = Instant_Noodles("Nongshim", "ramen", "shrimp")

  #brand
  #mynoodle.set_brand("nissin")
  #print(mynoodle.get_brand())

  #noodle type
  #mynoodle.set_noodle_type("udon")
  #print(mynoodle.get_noodle_type())

  #timer
  #print("I should microwave my noodles for:", mynoodle.get_timer(), "minutes")

  #noodletype
  #print(mynoodle.get_noodle_type())
  #mynoodle.set_noodle_type("udon")
  #print(mynoodle.get_noodle_type())

  #flavor
  #mynoodle.set_flavor("Chicken")
  #print(mynoodle.get_flavor())

  #other two methods
  #mynoodle.how_to_cook()
  #mynoodle.microwave(8)
  '''


if __name__ == "__main__":
    main()