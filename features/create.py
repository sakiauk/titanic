import pandas as pd

from base import Feature, get_arguments, generate_features

Feature.dir = 'features'

class FamilySize(Feature):
    def create_features(self):
        self.train['family_size'] = train['SibSp'] + train['Parch'] + 1
        self.test['family_size'] = test['SibSp'] + test['Parch'] + 1

if __name__ == '__main__':
    args = get_arguments()

    train = pd.read_csv('data/input/train.csv')
    test = pd.read_csv('data/input/test.csv')

    generate_features(globals(), args.force)