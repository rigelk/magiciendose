from centre.models import CentreAmbulatoire
from vaccin.models import Vaccin
import pandas
import numpy as np


def get_cva():
    df = pandas.read_excel("data/Referentiel_centres_vacci_20210421.xlsx")
    df.drop(df[~df.TYPOLOGIE.isin({'CVA', 'CV MIXTE'})].index, axis=0, inplace=True)
    df['Code'] = [str(e).zfill(5) for e in df.com_insee]
    return df


def peuple_centres():
    """
    Peupler la table CentreAmbulatoire

    :return:
    """
    df = get_cva()
    for _, el in df.iterrows():
        centre = CentreAmbulatoire(nom=el.nom, gid=el.gid, code_postal=el.com_cp,
                                   code_commune_insee=el.com_insee,
                                   capacite=np.random.randint(1000))
        centre.save()

    return


def peuple_vaccins():
    """
    Peupler la table Vaccin
    :return:
    """
    pfizer = Vaccin(nom="Pfizer", intervalle_injections=42)
    pfizer.save()
    moderna = Vaccin(nom="Moderna", intervalle_injections=28)
    moderna.save()
    az = Vaccin(nom="AstraZeneca", intervalle_injections=28)
    az.save()
