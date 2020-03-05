# Name and uwnetid: Adam Klingler, klinga@uw.edu
# Section: AB
# Description:

# Imports here
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Constants here
TRACTS = 'tl_2010_53_tract00/tl_2010_53_tract00.shp'
FOOD = 'food-access.csv'

# Functions here


def load_in_data(tracts, data):
    '''
    This function takes in a file for shape information and a file for census
    data and returns a GeoDataFrame with the values of both merged.
    '''
    tracts = gpd.read_file(tracts)
    data = pd.read_csv(data)

    gdata = tracts.merge(data, left_on='CTIDFP00', right_on='CensusTract',
                         how='left')

    return gdata


def percentage_food_data(gdata):
    '''
    This function returns the percentage of tracts that has food data
    associated.
    '''
    census_tracts = gdata['CensusTract']
    total_tracts, = census_tracts.shape
    data_tracts, = census_tracts.dropna().shape

    return data_tracts / total_tracts * 100


def plot_map(gdata):
    '''
    This function creates and saves a plot of the census tracts.
    '''
    fig, ax = plt.subplots(1)

    ax.set_title('Washington State Census Tracts')
    gdata.plot(ax=ax)
    fig.savefig('washington_population_map.png')


def plot_population_map(gdata):
    '''
    This function creates and saves a plot of the census tracts, color coded
    to the population living in each tract.
    '''
    fig, ax = plt.subplots(1)

    ax.set_title('Washington Population by Census Tract')
    gdata.plot(column='POP2010', legend='True', ax=ax)
    fig.savefig('washington_population_map.png')


def plot_population_county_map(gdata):
    '''
    This function creates and saves a plot of the counties, color coded to the
    population living in each county.
    '''
    counties = gdata[['County', 'POP2010', 'geometry']]
    counties = counties.dropna()

    pops = counties.dissolve(by='County', aggfunc='sum')

    fig, ax = plt.subplots(1)

    ax.set_title('Washington Population by County')
    pops.plot(column='POP2010', legend=True, ax=ax)
    fig.savefig('washington_county_population_map.png')


def plot_food_access_by_county(gdata):
    '''
    This function creates and saves a plot with four images, each color coded
    to the percentage of people with low access to food within half a mile,
    low access to food within half a mile and with low income, low access to
    food within 10 miles, and low access to food within 10 miles and with low
    income.
    '''
    slim_data = gdata[['County', 'geometry', 'POP2010', 'lapophalf', 'lapop10',
                       'lalowihalf', 'lalowi10']]

    adata = slim_data.dissolve(by='County', aggfunc='sum')
    pop = adata['POP2010']
    adata['lapophalf_ratio'] = adata['lapophalf'] / pop
    adata['lapop10_ratio'] = adata['lapop10'] / pop
    adata['lalowihalf_ratio'] = adata['lalowihalf'] / pop
    adata['lalowi10_ratio'] = adata['lalowi10'] / pop

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, figsize=(20, 10), ncols=2)

    ax1.set_title('Low Access: Half')
    adata.plot(column='lapophalf_ratio', ax=ax1, legend=True, vmin=0, vmax=1)

    ax2.set_title('Low Access + Low Income: Half')
    adata.plot(column='lalowihalf_ratio', ax=ax2, legend=True, vmin=0, vmax=1)

    ax3.set_title('Low Access: 10')
    adata.plot(column='lapop10_ratio', ax=ax3, legend=True, vmin=0, vmax=1)

    ax4.set_title('Low Access + Low Income: 10')
    adata.plot(column='lalowi10_ratio', ax=ax4, legend=True, vmin=0, vmax=1)

    fig.savefig('washington_county_food_access.png')


def plot_low_access_tracts(gdata):
    '''
    This function creates and saves a plot of all those census tracts, with
    tracts that have food data darkened and tracts with low access according
    to their urban / rural classification highlighted blue.
    '''
    clean_data = gdata.dropna()

    is_urban = clean_data['Urban'] == 1
    is_rural = clean_data['Rural'] == 1

    udata = clean_data[is_urban]
    rdata = clean_data[is_rural]

    is_la_urban = (udata['lapophalf'] > 500) | \
                  ((udata['lapophalf'] / udata['POP2010']) > 0.33)
    is_la_rural = (rdata['lapop10'] > 500) | \
                  ((rdata['lapop10'] / rdata['POP2010']) > 0.33)

    la_udata = udata[is_la_urban]
    la_rdata = rdata[is_la_rural]

    fig, ax = plt.subplots(1, figsize=(10, 5))

    ax.set_title('Low Access to Food based on Classifaction')
    gdata.plot(color='#EEEEEE', ax=ax)
    clean_data.plot(color='#AAAAAA', ax=ax)
    la_udata.plot(ax=ax)
    la_rdata.plot(ax=ax)
    fig.savefig('washington_low_access.png')


def main():
    '''
    This function runs several plotting functions over a data set to show low
    food access in different census plots around Washington.
    '''
    gdata = load_in_data(TRACTS, FOOD)

    percentage_food_data(gdata)
    plot_map(gdata)
    plot_population_map(gdata)
    plot_population_county_map(gdata)
    plot_food_access_by_county(gdata)
    plot_low_access_tracts(gdata)


if __name__ == "__main__":
    main()
