data sicne adlı py dosyasını çalıştırınca elde edeceginiz çıktılar bu şekilde olmalı 

C:\Users\MehmetDurmaz\PycharmProjects\dataScine\venv\Scripts\python.exe C:\Users\MehmetDurmaz\PycharmProjects\dataScine\Datascine.py 
            method  number  orbital_period   mass  distance  year
0  Radial Velocity       1         269.300   7.10     77.40  2006
1  Radial Velocity       1         874.774   2.21     56.95  2008
2  Radial Velocity       1         763.000   2.60     19.84  2011
3  Radial Velocity       1         326.030  19.40    110.62  2007
4  Radial Velocity       1         516.220  10.50    119.47  2009
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1035 entries, 0 to 1034
Data columns (total 6 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   method          1035 non-null   object 
 1   number          1035 non-null   int64  
 2   orbital_period  992 non-null    float64
 3   mass            513 non-null    float64
 4   distance        808 non-null    float64
 5   year            1035 non-null   int64  
dtypes: float64(3), int64(2), object(1)
memory usage: 48.6+ KB
None
method             object
number              int64
orbital_period    float64
mass              float64
distance          float64
year                int64
dtype: object
['Radial Velocity', 'Radial Velocity', 'Radial Velocity', 'Radial Velocity', 'Radial Velocity', ..., 'Transit', 'Transit', 'Transit', 'Transit', 'Transit']
Length: 1035
Categories (10, object): ['Astrometry', 'Eclipse Timing Variations', 'Imaging', 'Microlensing', ...,
                          'Pulsation Timing Variations', 'Radial Velocity', 'Transit',
                          'Transit Timing Variations']
(1035, 6)
                 count         mean  ...       75%       max
number          1035.0     1.785507  ...     2.000       7.0
orbital_period   992.0  2002.917596  ...   526.005  730000.0
mass             513.0     2.638161  ...     3.040      25.0
distance         808.0   264.069282  ...   178.500    8500.0
year            1035.0  2009.070531  ...  2012.000    2014.0

[5 rows x 8 columns]
True
method              0
number              0
orbital_period     43
mass              522
distance          227
year                0
dtype: int64
/////////////////////////////////////
None
method              0
number              0
orbital_period      0
mass              522
distance          227
year                0
dtype: int64
None 

method              0
number              0
orbital_period      0
mass                0
distance          227
year                0
dtype: int64 


Process finished with exit code 0
