from amocrm.v2 import tokens, Lead, Pipeline, Status, Company, Contact


tokens.default_token_manager(
    client_id="7a84e70e-249c-4eb3-9328-94d1a52001ec",
    client_secret="QMHnD2a8OarrN1cu9zSxX8F4PLfB5JhW2W9rihqGHwrv1ISjfoMJo2Fhr7yjWFjh",
    subdomain="8250",
    redirect_url="https://aktivkredit.ru/",
    storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
)
tokens.default_token_manager.init(code="def50200819ac3f7637afe97f520db9be262919bb4272ff6e6faad3c7354aa14b9d7e2cc9c9fdaed0d735b8900e413cf65940a0e581cb7cb05da4fb90836eb45892eddff617a15276f2b2e8e19362023c31ca64682b06c32226894157d854f76960b61bd440f2b345114aa5ac739760df95d04042b2a8a3db5b6e2cf0b921586d9b7f2fe78643d4e609376067472e0adcbe413139940ca5d726ca0df7d22cb0d10dd52a8755ca19ff378a93d48754ec08bc04aeae7ac35b63314f907ab693452a8b4d349859fa50e55eb39eaf66ac210b05fc62d9841975008307d336c8377dfe97c996a5d8151d5a3f2ce178f3cbeca587715e0e1128987c4ad9e7a99211df0d7c94f10e2d7647e8a5a17225a55d4a4a030b59c06fc287988928bcf1d8b130d19aa063f80a208805db67dbf50487cded9b778af13a910249d1abc016f951614130500019e87313e25069d5451b5eb50432ac06c00d45aa59ac5b73e62e1bedcc34e35e87ee1d468f4f751ebf7067d5d10d0aa4504ad8d51cb484ba80da8a59a59a0eab429e0978fef8d0341cd5879818c06c392b419223e5eb22d21197c3e7da38248bba961fb8a4fda31c0d01361dd91f098e43954e9a8627ef1c457947aee95c5f29a2e5872edfac9fcc49a5e48f131e51934c605e3e25c92f0a60908f9cf18e97bf67b40f18b", skip_error=False)