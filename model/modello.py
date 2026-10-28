from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito


'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # Connessione al DB + Controllo
        cnx = get_connection()
        result = []
        if cnx is None:
            return result
        # Cursore + query
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM strumento"
        # Prova query + struttura strumenti
        try:
            cursor.execute(query)
            for row in cursor:
                strumento = Strumento(row["id"], row["tipo"], row["marca"],
                                      row["anno_acquisto"], row["valore"], row["disponibile"] )
                result.append(strumento)

        except Exception as e:
            print(f"Errore nell'esecuzione della query: {e} ")
        finally:
            cursor.close()
            cnx.close()

        return result

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
