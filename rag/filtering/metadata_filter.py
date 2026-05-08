from rag.filtering.hierarchical_filter import (
    HierarchicalFilter,
)


class MetadataFilter:

    @staticmethod
    def apply(results, filters):

        filtered_results = []

        for result in results:

            match = True

            for key, value in filters.items():

                # -------------------------
                # Hierarchical category
                # -------------------------

                if key == "category":

                    allowed_categories = (
                        HierarchicalFilter.expand_category(
                            value
                        )
                    )

                    result_category = result.get(
                        "category"
                    )

                    if (
                        result_category
                        not in allowed_categories
                    ):

                        match = False
                        break

                # -------------------------
                # Standard filtering
                # -------------------------

                else:

                    if result.get(key) != value:

                        match = False
                        break

            if match:

                filtered_results.append(result)

        return filtered_results