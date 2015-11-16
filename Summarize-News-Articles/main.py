from frequency_summarize import FrequencySummarizer

text = '''
After witnessing his mother's (Michelle Harrison) supernatural murder and his father's (John Wesley Shipp) wrongful conviction for the crime, Barry Allen (Grant Gustin) is taken in by Detective Joe West (Jesse L. Martin) and his family. Allen becomes a brilliant but socially awkward crime scene investigator for the Central City Police Department. His obsession with his tragic past causes him to become an outcast among his peers; he investigates cold cases, paranormal occurrences, and cutting-edge scientific advancements that may shed light on his mother's murder. No one believes his description of the crime—that a ball of lightning with the face of a man invaded their home that night—and Allen is fiercely driven to vindicate himself and to clear his father's name. Fourteen years after his mother's death, an advanced particle accelerator malfunctions during its public unveiling, bathing the city center with a previously unknown form of radiation and creating a severe thunderstorm. Allen is struck by lightning from the storm and doused with chemicals in his lab. Awakening after a nine-month coma, he discovers he has the ability to move at superhuman speeds. Dr. Harrison Wells (Tom Cavanagh), the disgraced designer of the failed particle accelerator, describes Barry's special nature as "metahuman"; Allen soon discovers that he is not the only one who was changed by the radiation. Allen vows to use his gifts to protect Central City from the escalating violence of metahuman criminals. He is aided by a few close friends and associates who guard his secrets.
'''

fs = FrequencySummarizer()

for s in fs.summarize(text,5):
    print '*',s
