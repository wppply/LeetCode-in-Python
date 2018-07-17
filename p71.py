class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        folders = path.split('/')

        for folder in folders:
        	folder = folder.strip()
        	if folder == '.' or not folder: 
        		continue
        	elif folder == '..':
                    if len(stack)>0: 
                        stack.pop()
        	else:
        		stack.append(folder)
        return '/' + '/'.join(folder for folder in stack)
