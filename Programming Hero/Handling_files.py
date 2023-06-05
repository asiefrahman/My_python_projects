# opening file

objetfile = open('programming.txt')
p = objetfile.read()
print(p)

object = open('programming.txt', 'a')
object.write('\n')
object.close()

