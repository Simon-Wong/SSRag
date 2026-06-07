#这个文件可以是空的
from .SrcLoaderBase import BaseParameterSrc,BaseSrcLoader,BaseResultSrc
from .SrcLoaderBase import ResultSrc

from .SrcLoaderImp import ParameterSrcTxt,SrcLoaderTxt
from .SrcLoaderImp import ParameterSrcCSV,SrcLoaderCSV
from .SrcLoaderImp import ParameterSrcMD,SrcLoaderMD
from .SrcLoaderImp import ParameterSrcJSON,SrcLoaderJSON
from .SrcLoaderImp import ParameterSrcURL,SrcLoaderURL
from .SrcLoaderImp import ParameterSrcImageJpgPng,SrcLoaderImageJpgPng
from .SrcLoaderImp import ParameterSrcImageOCR,SrcLoaderImageOCR
from .SrcLoaderImp import ParameterSrcImageOCRModel,SrcLoaderImageOCRModel
from .SrcLoaderImp import ParameterSrcMHTML,SrcLoaderMHTML
from .SrcLoaderImp import ParameterSrcHTML,SrcLoaderHTML
from .SrcLoaderImp import ParameterSrcDocDocx,SrcLoaderDocDocx
from .SrcLoaderImp import ParameterSrcImageContent,SrcLoaderImageContent
from .SrcLoaderImp import ParameterSrcXlsXlsx,SrcLoaderXlsXlsx
