import pickle

questions = ["""
            Компания-разработчик Windows
            1) Mikrosoft
            2) Melkosoft
            3) Cybersoft
            4) Microsoft
            """,
            """
            Самая яблочная операционная система
            1) AppleOS
            2) Linux
            3) macOS
            4) FreeBSD
            """]
answers = [4, 1]
datafile = open("test.dat", "wb")
pickle.dump(questions, datafile)
pickle.dump(answers, datafile)
datafile.close()
