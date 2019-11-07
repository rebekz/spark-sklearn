from scipy.sparse import csr_matrix

from spark_sklearn.converter import Converter
from spark_sklearn.udt import CSRVectorUDT

__all__ = ['Converter', 'CSRVectorUDT']

csr_matrix.__UDT__ = CSRVectorUDT()
