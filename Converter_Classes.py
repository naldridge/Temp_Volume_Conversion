class Temp:

    def __init__(self, start_degrees=0, input_unit="", target_unit="", guess_target=0, answer_target=0):
        self.start_degrees = start_degrees
        self.input_unit = input_unit
        self.target_unit = target_unit
        self.guess_target = guess_target
        self.answer_target = answer_target
        
        
    def print_info(self):
        print(self.start_degrees, self.input_unit, self.guess_target, self.target_unit)
    
    #method to convert celsius to fahrenheit#
    def convert_c_to_f(self):
        return round(float(self.start_degrees * (9/5) + 32), 1)

    #method to convert celsius to kelvin#          
    def convert_c_to_k(self):
        return round(float(self.start_degrees + 273.15), 1)
        
    #method to convert celsius to rankine#
    def convert_c_to_r(self):
        return round(float(self.start_degrees * (9/5) + 491.67), 1) 
        
    def convert_f_to_c(self):
        return round(float((self.start_degrees - 32) * (5/9)), 1)
    
    def convert_f_to_k(self):
        return round(float((self.start_degrees - 32) * (5/9) + 273.15), 1)
  
    def convert_f_to_r(self):
        return round(float(self.start_degrees + 459.67), 1)

    def convert_k_to_c(self):
        return round(float(self.start_degrees - 273.15), 1)

    def convert_k_to_f(self):
        return round(float((self.start_degrees - 273.15) * (9/5) + 32), 1)

    def convert_k_to_r(self):
        return round(float(self.start_degrees * (9/5)), 1)
    
    def convert_r_to_c(self):
        return round(float((self.start_degrees - 491.67) * (5/9)), 1)

    def convert_r_to_f(self):
        return round(float(self.start_degrees - 459.67), 1)

    def convert_r_to_k(self):
        return round(float(self.start_degrees * (5/9)), 1)

    def validate_answer(self):
        if self.guess_target == self.answer_target:
            print("Correct!")
        else:
            print("Incorrect")

class Volume:
    def init(self, input_volume=0, input_unit="", target_unit="", guess_target=0, answer_target=0):
        self.input_volume = input_volume
        self.input_unit = input_unit
        self.target_unit = target_unit
        self.guess_target = guess_target
        self.answer_target = answer_target

    def convert_l_to_t(self):
         return round(float(self.input_volume * 67.628), 1)

    def convert_l_to_ci(self):
        return round(float(self.input_volume * 61.024), 1)
        
    def convert_l_to_c(self):
        return round(float(self.input_volume * 4.227), 1)
        
    def convert_l_to_cf(self):
        return round(float(self.input_volume / 28.317), 1)
        
    def convert_l_to_g(self):
        return round(float(self.input_volume / 3.785), 1)

    def convert_t_to_l(self):
        return round(float(self.input_volume / 67.628), 1)
   
    def convert_t_to_ci(self):
        return round(float(self.input_volume / 1.108), 1)
        
    def convert_t_to_c(self):
        return round(float(self.input_volume / 16), 1)

    def convert_t_to_cf(self):
        return round(float(self.input_volume / 1915), 1)

    def convert_t_to_g(self):
        return round(float(self.input_volume / 256), 1)

    def convert_ci_to_l(self):
        return round(float(self.input_volume / 61.024), 1)

    def convert_ci_to_t(self):
        return round(float(self.input_volume * 1.108), 1)
            
    def convert_ci_to_c(self):
        return round(float(self.input_volume / 14.438), 1)

    def convert_ci_to_cf(self):
        return round(float(self.input_volume / 1728), 1)

    def convert_ci_to_g(self):
        return round(float(self.input_volume / 231 ), 1)

    def convert_c_to_l(self):
        return round(float(self.input_volume / 4.227), 1)

    def convert_c_to_t(self):
        return round(float(self.input_volume * 16), 1)

    def convert_c_to_ci(self):
        return round(float(self.input_volume * 14.438), 1)

    def convert_c_to_cf(self):
        return round(float(self.input_volume / 120), 1)

    def convert_c_to_g(self):
        return round(float(self.input_volume / 16), 1)

    def convert_cf_to_l(self):
        return round(float(self.input_volume / 28.317), 1)

    def convert_cf_to_t(self):
        return round(float(self.input_volume * 1915), 1)

    def convert_cf_to_ci(self):
        return round(float(self.input_volume * 1728), 1)
        
    def convert_cf_to_c(self):
        return round(float(self.input_volume / 120), 1)

    def convert_cf_to_g(self):
        return round(float(self.input_volume * 7.481), 1)

    def convert_g_to_l(self):
        return round(float(self.input_volume * 3.785), 1)

    def convert_g_to_t(self):
        return round(float(self.input_volume * 256), 1)

    def convert_g_to_ci(self):
        return round(float(self.input_volume * 231), 1)

    def convert_g_to_c(self):
        return round(float(self.input_volume * 16), 1)

    def convert_g_to_cf(self):
        return round(float(self.input_volume / 7.481), 1)

    def validate_answer(self):
        if type(self.guess_target)==float and self.guess_target == self.answer_target:
            print("Correct!")
        elif type(self.guess_target)!=float:
            print("Invalid Answer")
        else:
            print("Incorrect")

        