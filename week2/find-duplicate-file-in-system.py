class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        stored_files = {}

        for i in paths:
            files = i.split(" ")
            source = files[0]

            files_with_content = files[1:]
            for file in files_with_content:    
                filename , content = file.split("(")
                content = content[:-1]

                if content in stored_files:
                    stored_files[content].append(source+"/"+ filename)
                else:
                    stored_files[content] = [source+"/"+filename]


        duplicate_files = []
        for file in stored_files:
            if len(stored_files[file]) > 1:
                duplicate_files.append(stored_files[file])

        return duplicate_files