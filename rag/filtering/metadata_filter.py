class MetadataFilter:

    @staticmethod
    def apply(results, filters):

        filtered_results = []

        for result in results:

            match = True

            for key, value in filters.items():

                if result.get(key) != value:
                    match = False
                    break

            if match:
                filtered_results.append(result)

        return filtered_results