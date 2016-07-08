def smiles_feature(unicode_message, unicode_smiles):
    total = 0
    for smile in unicode_smiles:
        total += unicode_message.count(smile)
        unicode_message.replace(smile, '')
    return total
# usage
positive = Features.smiles_feature(unicode_message, smiles['positive_values'])
negative = -Features.smiles_feature(unicode_message, smiles['negative_values'])
