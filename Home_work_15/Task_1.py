import logging


# Настройка логирования

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Форматтер для сообщений

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для сообщений уровня DEBUG и INFO

debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)
logger.addHandler(debug_info_handler)

# Обработчик для сообщений уровня WARNING и выше

warnings_error_handler = logging.FileHandler('warnings_errors.log')
warnings_error_handler.setLevel(logging.WARNING)
warnings_error_handler.setFormatter(formatter)
logger.addHandler(warnings_error_handler)

# Логирование сообщенгий различных уровней
logger.debug('Это сообщение уровня DEBUG')
logger.info('Это сообщение уровня INFO')
logger.warning('Это соообщение уровня WARNING')
logger.error('Это сообщение уровня ERROR')
logger.critical('Это соообщение уровня CRITICAL')