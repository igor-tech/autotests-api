import logging

logger = logging.getLogger("AUTOTEST")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler.setFormatter(formater)

logger.addHandler(handler)

logger.debug("Это сообщение уровня дебаг")
logger.info("Это сообщение уровня info")
logger.warning("Это сообщение уровня warning")
logger.error("Это сообщение уровня error")