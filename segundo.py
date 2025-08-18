from codecs import ignore_errors


nome = input ("qual seu nome?")
endereco = input ("qual teu endereço?")
cidade = input ("qual sua cidade?")
cep = int (input ("qual seu cep?"))
dian = int (input ("qual seu dia de nascimento?"))
mesn = int (input ("qual seu mês de nascimento?"))
anon = int (input ("qual seu ano de nascimento?"))
print ("seu nome é", nome)
print ("sua cidade é", cidade)
print ("sua teu endereço é", endereco)
print ("seu cep é", cep)
print ("sua data de nascimento é", dian,"/", mesn,"/", anon,"/")