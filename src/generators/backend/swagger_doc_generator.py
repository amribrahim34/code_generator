class SwaggerDocGenerator:
    @staticmethod
    def generate_swagger_doc(model: dict) -> str:
        return f"""/**
     * @OA\\Tag(
     *     name="{model['name']}s",
     *     description="{model['name']} resource"
     * )
     */"""

    @staticmethod
    def generate_index_doc(model: dict) -> str:
        return f"""
    /**
     * @OA\\Get(
     *     path="/{model['name'].lower()}s",
     *     tags={{"{model['name']}s"}},
     *     summary="Get list of {model['name']}s",
     *     description="Returns list of {model['name']}s",
     *     @OA\\Response(
     *         response=200,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_store_doc(model: dict) -> str:
        return f"""
    /**
     * @OA\\Post(
     *     path="/{model['name'].lower()}s",
     *     tags={{"{model['name']}s"}},
     *     summary="Store a new {model['name']}",
     *     description="Returns {model['name']} data",
     *     @OA\\RequestBody(
     *         required=true,
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}StoreRequest")
     *     ),
     *     @OA\\Response(
     *         response=201,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_show_doc(model: dict) -> str:
        return f"""
    /**
     * @OA\\Get(
     *     path="/{model['name'].lower()}s/{{id}}",
     *     tags={{"{model['name']}s"}},
     *     summary="Get {model['name']} information",
     *     description="Returns {model['name']} data",
     *     @OA\\Parameter(
     *         name="id",
     *         description="{model['name']} id",
     *         required=true,
     *         in="path",
     *         @OA\\Schema(
     *             type="integer"
     *         )
     *     ),
     *     @OA\\Response(
     *         response=200,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_update_doc(model: dict) -> str:
        return f"""
    /**
     * @OA\\Put(
     *     path="/{model['name'].lower()}s/{{id}}",
     *     tags={{"{model['name']}s"}},
     *     summary="Update existing {model['name']}",
     *     description="Returns updated {model['name']} data",
     *     @OA\\Parameter(
     *         name="id",
     *         description="{model['name']} id",
     *         required=true,
     *         in="path",
     *         @OA\\Schema(
     *             type="integer"
     *         )
     *     ),
     *     @OA\\RequestBody(
     *         required=true,
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}UpdateRequest")
     *     ),
     *     @OA\\Response(
     *         response=200,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_destroy_doc(model: dict) -> str:
        return f"""
    /**
     * @OA\\Delete(
     *     path="/{model['name'].lower()}s/{{id}}",
     *     tags={{"{model['name']}s"}},
     *     summary="Delete existing {model['name']}",
     *     description="Deletes a record and returns no content",
     *     @OA\\Parameter(
     *         name="id",
     *         description="{model['name']} id",
     *         required=true,
     *         in="path",
     *         @OA\\Schema(
     *             type="integer"
     *         )
     *     ),
     *     @OA\\Response(
     *         response=204,
     *         description="Successful operation",
     *         @OA\\JsonContent()
     *     )
     * )
     */"""