from rag.filtering.hierarchical_filter import (
    HierarchicalFilter,
)


class MetadataFilter:

    @staticmethod
    def apply(
        results,
        filters,
    ):

        filtered_results = []

        for result in results:

            matched = True

            for key, value in filters.items():

                result_value = result.get(key)

                # ---------------------------------
                # Hierarchical category filtering
                # ---------------------------------

                if key == "category":

                    expanded_categories = []

                    # Support both string and list
                    if isinstance(value, list):

                        for item in value:

                            expanded_categories.extend(
                                HierarchicalFilter.expand_category(
                                    item
                                )
                            )

                    else:

                        expanded_categories = (
                            HierarchicalFilter.expand_category(
                                value
                            )
                        )

                    if result_value not in expanded_categories:

                        matched = False
                        break

                # ---------------------------------
                # Generic filtering
                # ---------------------------------

                else:

                    if isinstance(value, list):

                        if result_value not in value:

                            matched = False
                            break

                    else:

                        if result_value != value:

                            matched = False
                            break

            if matched:

                filtered_results.append(result)

        return filtered_results