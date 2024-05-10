# Funktionsnamn
def stringt(*args, sep=" ", end="\n"):
    """
    Function similar to print() but returns a string instead of printing it.

    Args:
        *args: Any number of positional arguments, treated as strings.
        sep (str, optional): Text separator to be used between each
        argument. Defaults to " ".

        end (str, optional): End string to  be appended
        at the end of the final string.
        Defaults to "\n".

    Returns:
        str: A string consisting of all positional arguments
        concatenated with
        the separator sep between each argument,
        and with end appended at the end.
    """
    # Konvertera alla argument till strängar
    string_args = [str(arg) for arg in args]

   # Sammanfoga de strängargumenten med hjälp av avgränsaren
    result = sep.join(string_args)

    # Lägg till slutsträngen
    result += end

    # Returnera den slutgiltiga strängen
    return result


# end="\n" betyder att standardvärdet för end är en ny rad ("\n"). 
#Det betyder att om end inte ges något annat värde när funktionen stringt() anropas,
#kommer en ny rad att läggas till i slutet av den resulterande strängen.

#Standardvärdet för sep är ett mellanslag, Du kan även lägga till t.ex , mellan orden.
 
print(stringt("Hej", "världen", sep=", ", end="!!!"))  # Ska bli: "Hej, världen!"
print(stringt("Python", "är", "kul"))  # Ska bli: "Python är kul\n"
print(stringt("En", "två", "tre", sep=" - "))  # Ska bli: "En - två - tre\n"
print(stringt("Slut", end="."))  # Ska bli: "Slut."
print(stringt("Ett roligt", " argument", sep=","))  # Ska bli: "Ettargument\n"
print(stringt("Ensam"))  # Ska bli: "Ensam\n" 