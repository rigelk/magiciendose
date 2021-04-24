# A executer depuis python manage.py shell
from collections import defaultdict

from centre.models import CentreAmbulatoire
import pandas, geopandas
import numpy as np
from shapely.ops import nearest_points


def get_cva():
    df = pandas.read_excel("Referentiel_centres_vacci_20210421.xlsx")
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
        centre = CentreAmbulatoire(nom=el.nom, id_ministere=el.gid, code_postal=el.com_cp,
                                   code_commune_insee=el.com_insee,
                                   capacite=np.random.randint(1000))
        centre.save()

    return


def get_enum_depts():
    """
    Retourne une enumeration des departements francais
    :return:
    """
    df = pandas.read_csv("departements-francais.csv", delimiter="\t")
    df['dept'] = [str(e).zfill(2) for e in df['NUMÉRO']]
    df.drop([101, 102], axis=0, inplace=True)
    enum_dept = [("{} - {}".format(e.dept, e.NOM), i + 1) for i, e in df.iterrows()]

    return enum_dept


def get_enum_regions():
    """
    Retourne une enumeration des departements francais
    :return:
    """
    df = pandas.read_csv("region2020.csv", delimiter=",")
    df['region'] = [str(e).zfill(2) for e in df['reg']]
    enum_region = [(i + 1, "{} - {}".format(e.region, e.libelle),) for i, e in df.iterrows()]

    return enum_region


# Maintenant on va proposer une repartition des doses en fonction de la pop
def get_df_communes(region_filtre=11):
    df = pandas.read_excel('Donnes_INSEE_NumEduc.xlsx')
    df['Code'] = [str(e).zfill(5) for e in df.Code]
    latlon = pandas.read_csv('communes-departement-region.csv')
    latlon.drop_duplicates(['code_commune_INSEE', 'latitude', 'longitude', 'code_region'], inplace=True, keep='first')
    df = df.merge(latlon[['code_commune_INSEE', 'latitude', 'longitude', 'code_region']], left_on='Code',
                  right_on='code_commune_INSEE', how='inner')

    if region_filtre is not None:
        df.drop(df[df.code_region != region_filtre].index, axis=0, inplace=True)
    df.drop('code_commune_INSEE', axis=1, inplace=True)

    return df


def get_alone_com():
    df = get_df_communes(region_filtre=11)
    cva = get_cva()
    num_centres = cva.groupby('Code', as_index=False).gid.count()

    df = df.merge(num_centres, on='Code', how='left')
    df.gid.fillna(0, inplace=True)
    return df


def get_closest_centre():
    df = get_alone_com()
    cva = get_cva()

    gdf = geopandas.GeoDataFrame(
        df, geometry=geopandas.points_from_xy(df.longitude, df.latitude))

    gcva = geopandas.GeoDataFrame(
        cva, geometry=geopandas.points_from_xy(cva.long_coor1, cva.lat_coor1))
    centres = gcva.geometry.unary_union

    def near(point, pts=centres):
        # find the nearest point and return the corresponding Place value
        nearest = gcva.geometry == nearest_points(point, pts)[1]
        return gcva[nearest].gid.values[0]

    gdf['Plus_proche'] = gdf.apply(lambda row: near(row.geometry), axis=1)
    gdf.loc[gdf.gid > 0, 'Plus_proche'] = None
    return gdf


def get_pop_centre():
    cva = get_cva()
    gdf = get_closest_centre()

    result = defaultdict(list)
    pop_tot = 0
    for i, el in cva.iterrows():
        gid = el.gid
        pop_proches = gdf[gdf.Plus_proche == gid].Population2016.sum()
        pop_commune = gdf[gdf.Code == el.Code].Population2016.values[0] / gdf[gdf.Code == el.Code].gid.values[0]

        result['gid'].append(gid)
        result['Population'].append(pop_commune + pop_proches)
        pop_tot += result['Population'][-1]

    result = pandas.DataFrame.from_dict(result)
    cva = cva.merge(result, on='gid', how='inner')
    cva = cva.merge(cva.groupby('DEPT', as_index=False).Population.sum(), on='DEPT', suffixes=('_centre', '_dept'))
    cva['ratio'] = cva.Population_centre/cva.Population_dept*100
    return cva
