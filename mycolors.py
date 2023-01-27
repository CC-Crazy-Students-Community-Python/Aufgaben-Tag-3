from os import system

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

system( "cls" )

def colors( color ):
    color = color.lower()
    match color:
        case "reset":
            return "\033[0m reset: \t\033[90m \\033[0m\033[00m" .format( input )
        case "bold":
            return "\033[01m bold: \t\033[90m \\033[01m\033[00m" .format( input )
        case "disable":
            return "\033[02m disable: \t\033[90m \\033[02m\033[00m" .format( input )
        case "underline":
            return "\033[04m underline: \t\033[90m \\033[04m\033[00m" .format( input )
        case "reverse":
            return "\033[07m reverse: \t\033[90m \\033[07m\033[00m" .format( input )
        case "strikethrough":
            return "\033[09m strikethrough: \t\033[90m \\033[09m\033[00m" .format( input )
        case "invisible":
            return "\033[08m invisible: \t\033[90m \\033[08m\033[00m" .format( input )
        case "black":
            return "\033[30m black: \t\033[90m \\033[30m\033[00m" .format( input )
        case "red":
            return "\033[31m red: \t\033[90m \\033[31m\033[00m" .format( input )
        case "green":
            return "\033[32m green: \t\033[90m \\033[32m\033[00m" .format( input )
        case "orange":
            return "\033[33m orange: \t\033[90m \\033[33m\033[00m" .format( input )
        case "blue":
            return "\033[34m blue: \t\033[90m \\033[34m\033[00m" .format( input )
        case "purple":
            return "\033[35m purple: \t\033[90m \\033[35m\033[00m" .format( input )
        case "cyan":
            return "\033[36m cyan: \t\033[90m \\033[36m\033[00m" .format( input )
        case "lightgrey":
            return "\033[37m lightgrey: \t\033[90m \\033[37m\033[00m" .format( input )
        case "darkgrey":
            return "\033[90m darkgrey: \t\033[90m \\033[90m\033[00m" .format( input )
        case "lightred":
            return "\033[91m lightred: \t\033[90m \\033[91m\033[00m" .format( input )
        case "lightgreen":
            return "\033[92m lightgreen: \t\033[90m \\033[92m\033[00m" .format( input )
        case "yellow":
            return "\033[93m yellow: \t\033[90m \\033[93m\033[00m" .format( input )
        case "lightblue":
            return "\033[94m lightblue: \t\033[90m \\033[94m\033[00m" .format( input )
        case "pink":
            return "\033[95m pink: \t\033[90m \\033[95m\033[00m" .format( input )
        case "lightcyan":
            return "\033[96m lightcyan: \t\033[90m \\033[96m\033[00m" .format( input )
        case other:
            return "\033[0m reset: \t\t\033[90m \\033[0m\033[00m\n\033[01m bold: \t\t\t\033[90m \\033[01m\033[00m\n\033[02m disable: \t\t\033[90m \\033[02m\033[00m\n\033[04m underline: \t\t\033[90m \\033[04m\033[00m\n\033[07m reverse: \t\t\033[90m \\033[07m\033[00m\n\033[09m strikethrough: \t\033[90m \\033[09m\033[00m\n\033[08m invisible: \t\t\033[90m \\033[08m\033[00m\n\n\033[30m black: \t\t\033[90m \\033[30m\033[00m\n\033[31m red: \t\t\t\033[90m \\033[31m\033[00m\n\033[32m green: \t\t\033[90m \\033[32m\033[00m\n\033[33m orange: \t\t\033[90m \\033[33m\033[00m\n\033[34m blue: \t\t\t\033[90m \\033[34m\033[00m\n\033[35m purple: \t\t\033[90m \\033[35m\033[00m\n\033[36m cyan: \t\t\t\033[90m \\033[36m\033[00m\n\033[37m lightgrey: \t\t\033[90m \\033[37m\033[00m\n\033[90m darkgrey: \t\t\033[90m \\033[90m\033[00m\n\033[91m lightred: \t\t\033[90m \\033[91m\033[00m\n\033[92m lightgreen: \t\t\033[90m \\033[92m\033[00m\n\033[93m yellow: \t\t\033[90m \\033[93m\033[00m\n\033[94m lightblue: \t\t\033[90m \\033[94m\033[00m\n\033[95m pink: \t\t\t\033[90m \\033[95m\033[00m\n\033[96m lightcyan: \t\t\033[90m \\033[96m\033[00m\n"
            
if __name__ == "__main__":
    print( colors( "default" ) )