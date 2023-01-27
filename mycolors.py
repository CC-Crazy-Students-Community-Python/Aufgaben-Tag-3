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

def colors( color ):
    match color:
        case "red":  return "\\033[91m{ITS RED}\\033[00m"
        case "green": return "\\033[92m{ITS GREEN}\\033[00m"
        case "yellow": return "\\033[93m{ITS YELLOW}\\033[00m"
        case "lightpurple": return "\\033[94m{ITS LIGHTPURPLE}\\033[00m"
        case "purple": return "\\033[95m{ITS PURPLE}\\033[00m"
        case "cyan": return "\\033[96m{ITS CYAN}\\033[00m"
        case "gray": return "\\033[97m{ITS GRAY}\\033[00m"
        case "black": return "\\033[98m{ITS BLACK}\\033[00m"
		case other:
			return "\\033[91m{ITS RED}\\033[00m"
			return "\\033[92m{ITS GREEN}\\033[00m"
			return "\\033[93m{ITS YELLOW}\\033[00m"
			return "\\033[94m{ITS LIGHTPURPLE}\\033[00m"
			return "\\033[95m{ITS PURPLE}\\033[00m"
			return "\\033[96m{ITS CYAN}\\033[00m"
			return "\\033[97m{ITS GRAY}\\033[00m"
			return "\\033[98m{ITS BLACK}\\033[00m"


if __name__ == "__main__":
    doctest.testmod()