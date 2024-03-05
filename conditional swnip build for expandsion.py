 for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
        
        if operation == "Add":
            result_list.insert(tk.END, num + current_val)
        elif operation == "Subtract":
            result_list.insert(tk.END, num - current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "Divide":
            if current_val != 0:
                result_list.insert(tk.END, num / current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")
        if operation == "log10":
            current_val = math.log10(num)
            result_list.insert(tk.END, current_val)
        elif operation == "log":
            result_list.insert(tk.END, math.log(num, current_val)
        elif operation == "Multiply":
        
         if operation == "Add":
            result_list.insert(tk.END, num + current_val)
        elif operation == "Subtract":
            result_list.insert(tk.END, num - current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "Divide":
            if current_val != 0:
                result_list.insert(tk.END, num / current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")

        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
         
        elif operation == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_val))

    txt.insert("1.0", result_list.get(0, tk.END))
    
        if operation == "Add":
            result_list.insert(tk.END, num + current_val)
        elif operation == "Subtract":
            result_list.insert(tk.END, num - current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "Divide":
            if current_val != 0:
                result_list.insert(tk.END, num / current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")

        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
         
        elif operation == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_val))

    txt.insert("1.0", result_list.get(0, tk.END))



        if operation == "log10":
            current_val = math.log10(num)
            result_list.insert(tk.END, current_val)
        elif operation == "log":
            result_list.insert(tk.END, math.log(num, current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "1/X":
            if current_val != 0:
                result_list.insert(tk.END, 1/current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")

        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
         












        if additional_op == "Add":
            result_list.delete(i)
            result_list.insert(i, current_result + additional_num)
        elif additional_op == "Subtract":
            result_list.delete(i)
            result_list.insert(i, current_result - additional_num)
        elif additional_op == "Multiply":
            result_list.delete(i)
            result_list.insert(i, current_result * additional_num)
        elif additional_op == "Divide":
            result_list.delete(i)
            if additional_num != 0:
                result_list.insert(i, current_result / additional_num)

            else:
                result_list.insert("end", "Can not be Zero")
       

        elif additional_op == "Power of":
            result_list.delete(i)
            result_list.insert(i, current_result ** additional_num)


        elif additional_op == "SQRT of":
            result_list.delete(i)
            result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))
        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
          for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
        
             elif operation == "SQRT of":
                result_list.delete(i)
                res if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))ult_list.insert(i, math.sqrt(current_val))

    txt.insert("1.0", result_list.get(0, tk.END))

    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "sin":
                result_list.delete(i)
                result_list.insert(i, math.sin(current_result)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
          txt.insert("1.0", result_list.get(0, tk.END))         
        elif operation == if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END)) "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_val))

    txt.insert("1.0", result_list.get(0, tk.END))

    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
   if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))          for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
        
    
    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))          for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
    
    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))          for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
        
        if operation == "Add":
            result_list.insert(tk.END, num + current_val)
        elif operation == "Subtract":
            result_list.insert(tk.END, num - current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "Divide":
            if current_val != 0:
                result_list.insert(tk.END, num / current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")

        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
         
        elif operation == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_val))

    txt.insert("1.0", result_list.get(0, tk.END))

    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))          for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
        
        if operation == "Add":
            result_list.insert(tk.END, num + current_val)
        elif operation == "Subtract":
            result_list.insert(tk.END, num - current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "Divide":
            if current_val != 0:
                result_list.insert(tk.END, num / current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")

        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
         
        elif operation == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_val))

    txt.insert("1.0", result_list.get(0, tk.END))

    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))          for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
        
        if operation == "Add":
            result_list.insert(tk.END, num + current_val)
        elif operation == "Subtract":
            result_list.insert(tk.END, num - current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "Divide":
            if current_val != 0:
                result_list.insert(tk.END, num / current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")

        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
         
        elif operation == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_val))

    txt.insert("1.0", result_list.get(0, tk.END))

    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))
    txt.insert("1.0", result_list.get(0, tk.END))         
