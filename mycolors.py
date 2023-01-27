def red( input ):
    return "\033[91m{}\033[00m" .format( input )
def green( input ):
    return "\033[92m{}\033[00m" .format( input )
def yellow( input ):
    return "\033[93m{}\033[00m" .format( input )
def lightpurple( input ):
    return "\033[94m{}\033[00m" .format( input )
def purple( input ):
    return "\033[95m{}\033[00m" .format( input )
def cyan( input ):
    return "\033[96m{}\033[00m" .format( input )
def gray( input ):
    return "\033[97m{}\033[00m" .format( input )
def black( input ):
    return "\033[98m{}\033[00m" .format( input )

from os import system

def colors( color ):
    system( "cls" )
    color = color.lower()
    match color:
        case "red":
            return "\033[91m RED: \t\t\033[92m \\033[91m"
        case "green":
            return "\033[92m GREEN: \t\033[92m \\033[92m"
        case "yellow":
            return "\033[93m YELLOW: \t\033[92m \\033[93m"
        case "lightpurple":
            return "\033[94m LIGHTPURPLE: \t\033[92m \\033[94m"
        case "purple":
            return "\033[95m PURPLE: \t\033[92m \\033[95m"
        case "cyan":
            return "\033[96m CYAN: \t\t\033[92m \\033[96m"
        case "gray" | "lightgray":
            return "\033[97m LIGHTGRAY: \t\033[92m \\033[97m"
        case "black":
            return "\033[98m BLACK: \t\033[92m \\033[98m"
        case "close" | "ende" | "end" | "default":
            return "\033[00m DEFAULT: \t\033[92m \\033[00m\033[00m"
        case other:
            return "\033[91m RED: \t\t\033[92m \\033[91m\n\033[92m GREEN: \t\033[92m \\033[92m\n\033[93m YELLOW: \t\033[92m \\033[93m\n\033[94m LIGHTPURPLE: \t\033[92m \\033[94m\n\033[95m PURPLE: \t\033[92m \\033[95m\n\033[96m CYAN: \t\t\033[92m \\033[96m\n\033[97m LIGHTGRAY: \t\033[92m \\033[97m\n\033[98m BLACK: \t\033[92m \\033[98m\n\033[00m DEFAULT: \t\033[92m \\033[00m\033[00m"
if __name__ == "__main__":
    print( colors( "0" ) )