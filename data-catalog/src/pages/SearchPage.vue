<template>
    <div>
        <AppHeader />
        <div class="filter-container">
            <b-col class="my-1" lg="6">
                <b-form-group class="mb-0" label="Filter" label-align-sm="right" label-cols-sm="3"
                    label-for="filter-input" label-size="sm">
                    <b-input-group size="sm">
                        <b-form-input id="filter-input" v-model="filter" placeholder="Type to Search"
                            type="search"></b-form-input>
                        <b-input-group-append>
                            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                        </b-input-group-append>
                    </b-input-group>
                </b-form-group>
            </b-col>
            <b-col class="my-1" lg="6">
                <b-form-group v-slot="{ ariaDescribedby }" v-model="sortDirection" class="mb-0"
                    description="Leave all unchecked to filter on all data" label="Filter On" label-align-sm="right"
                    label-cols-sm="3" label-size="sm">
                    <b-form-checkbox-group v-model="filterOn" :aria-describedby="ariaDescribedby" class="mt-1">
                        <b-form-checkbox value="molecule_name">Molecule Name</b-form-checkbox>
                        <b-form-checkbox value="absorb">Absorb</b-form-checkbox>
                        <b-form-checkbox value="year_publ">Year of Publication</b-form-checkbox>
                        <br />
                        <b-form-checkbox value="lifetime">Life Time</b-form-checkbox>
                        <b-form-checkbox value="comp_class">Compound Class</b-form-checkbox>
                    </b-form-checkbox-group>
                </b-form-group>
            </b-col>
        </div>

        <!-- New Filter Container -->
        <div class="filter-container">
            <strong>New Data Filter</strong>
            <div>
                <table>
                    <tr>
                        <td>
                            <b-button variant="primary">AND</b-button>
                            <b-button variant="primary">OR</b-button>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <b-form-select v-model="propertyNameselected" :options="propertyName"></b-form-select>
                        </td>
                        <td>
                            <b-form-select v-model="propertyInstanceselected" :options="propertyInstance"></b-form-select>
                        </td>
                        <td>
                            <b-form-input v-model="inputField" placeholder="Enter option" required></b-form-input>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <b-button variant="primary">Search</b-button>
                            <b-button variant="danger">Delete</b-button>
                        </td>
                    </tr>
                </table>
                <div class="mt-3">Selected: <strong>{{ propertyNameselected }}, {{ propertyInstanceselected }}</strong></div>
            </div>
        </div>
        <!-- End of New Filter Container -->

        <!-- Table Property - 2 -->

        <!-- End of Table Property - 2 -->

        <div class="table-container justify-content-md-center table-bordered table-hover">
            <b-table id="my-table" :current-page="currentPage" :fields="fields" :filter="filter"
                :filter-included-fields="filterOn" :items="items" :per-page="perPage" caption-top responsive small>
                <template #table-caption>
                    <p id="table-caption">
                        <strong>Total No.of Records found in Experimental Database:
                            {{ rows }}</strong>
                        <br />
                        <strong>Filtered Results: {{ filteredItems }}</strong>
                    </p>
                </template>
                <template #cell(mol_id)="data">
                    <a href="#" @click="onChange">{{ data.value }}</a>
                </template>
            </b-table>
        </div>
        <b-pagination v-model="currentPage" :per-page="perPage" :total-rows="rows" align="right"
            aria-controls="my-table" class="pagination" />

    </div>
</template>

<script>
// import AppHeader from "@/components/AppHeader";
import axios from "axios";
import DataSheet from "@/pages/DataSheet";
import AccountInfo from "@/pages/AccountInfo";
// import DataTable from './DataTable.vue';

export default {
    name: "SearchPage",
    // eslint-disable-next-line vue/no-unused-components
    components: { AccountInfo, DataSheet },
    data() {
        return {
            fields: [
                {
                    key: "molecule_id",
                    sortable: true,
                },
                {
                    key: "molecule_name",
                    sortable: true,
                },
                {
                    key: "jour_cit",
                },
                {
                    key: "mw_source",
                    sortable: true,
                },
                {
                    key: "absorb",
                    sortable: true,
                },
                {
                    key: "journal",
                },
                {
                    key: "lifetime",
                },
                {
                    key: "emp_formula_sort",
                },
                {
                    key: "year_publ",
                },
            ],
            items: [],
            filter: null,
            filterOn: [],
            perPage: 15,
            currentPage: 1,
            displayCategory: false,
            propertyNameselected: null,
            propertyInstanceselected: null,
            propertyName: [
                { value: 'molecule_name', text: "Molecule Name" },
                { value: 'absorb', text: "Absorb"}
            ],
            propertyInstance: [
                { value: 'lessthan', text: 'Lessthan' },
                { value: 'greaterthan', text: 'Greaterthan'}
            ]
        };
    },

    async created() {
        try {
            const res = await axios.get(`http://127.0.0.1:8000/api/ExpDB/`);
            this.items = res.data;
        } catch (error) {
            console.log(error);
        }
    },
    watch: {

    },
    computed: {
        rows() {
            return this.items.length;
        },
        filteredItems() {
            return this.filterOn.length;
        },
    },
    methods: {
        onChange(event) {
            this.subDrop = this.sub_drop_values[event.target.value];
        },
    },
};
</script>

<style scoped>
.filter-container {
    padding: 2% 2%;
    margin: 3% 20%;
    background-color: #f8f9fa;
}

.btn-right {
    float: right;
    margin-left: 2%;
}

.opt-container {
    height: 40px;
    display: inline-flex;
    border-style: solid;
    border-width: 1px;
    border-color: #007bff;
    background-color: white;
    border-radius: 10px;
    align-items: center;
}

.dropdown {
    align-items: center;
}

.table-container {
    padding-bottom: unset;
    margin-left: 4%;
    margin-right: 4%;
    margin-bottom: unset;
}

.pagination {
    margin-right: 4%;
}

.dropdown-item {
    color: black;
}

#table-caption {
    text-align: center;
}
</style>
