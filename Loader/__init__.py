#这个文件可以是空的
from .LoaderBase import BaseParameterLoader,BaseLoader,BaseResultLoader
from .LoaderBase import ResultLoader

from .LoaderImp import ParameterLoaderTxt,LoaderTxt
from .LoaderImp import ParameterLoaderCSV,LoaderCSV
from .LoaderImp import ParameterLoaderMD,LoaderMD
from .LoaderImp import ParameterLoaderJSON,LoaderJSON
from .LoaderImp import ParameterLoaderURL,LoaderURL
from .LoaderImp import ParameterLoaderImageJpgPng,LoaderImageJpgPng
from .LoaderImp import ParameterLoaderImageOCR,LoaderImageOCR
from .LoaderImp import ParameterLoaderImageOCRModel,LoaderImageOCRModel
from .LoaderImp import ParameterLoaderMHTML,LoaderMHTML
from .LoaderImp import ParameterLoaderHTML,LoaderHTML
from .LoaderImp import ParameterLoaderDocDocx,LoaderDocDocx
from .LoaderImp import ParameterLoaderImageContent,LoaderImageContent
from .LoaderImp import ParameterLoaderXlsXlsx,LoaderXlsXlsx
from .LoaderImp import ParameterLoaderPDFModel,LoaderPDFModel
from .LoaderImp import ParameterLoaderPDF,LoaderPDF
from .LoaderImp import ParameterLoaderPPT,LoaderPPT
