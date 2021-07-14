import ctypes
import sys

def main():
	userDLL_handle = ctypes.WindDLL('User32.dll')
	kernelDLL_handle = ctypes.WindDLL('Kernel32.dll')
	PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
	lpClassName = None
	applicationName = input('Enter Application Name: ').encode('utf-8')
	lpWindowName = ctypes.c_char_p(applicationName)
	HWND = userDLL_handle.FindWindowA(lpClassName, lpWindowName)	
	lpdwProcessID = ctypes.c_ulong()
	DWORD = userDLL_handle.GetWindowThreadProcessId(HWND, ctypes.byref(lpdwProcessID))
	dwDesiredAccess = PROCESS_ALL_ACCESS
	bInheritHandle = False
	dwProcessID = lpdwProcessID
	process_handler = kernelDLL_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessID)
	exitCode = 0x1
	errorCode = kernelDLL_handle.TerminateProcess(process_handler, exitCode)

if __name__ == '__main__':
	main()