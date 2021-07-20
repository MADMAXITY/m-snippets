import generator

file = generator.main()
outfile = open("out1.pdf", "wb+")
outfile.write(file)
outfile.close()
