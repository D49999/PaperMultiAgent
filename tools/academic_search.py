class AcademicSearchTool:
    def search(self, query):
        print(f"  [Tool: AcademicSearch] 正在检索关键词: {query}")
        return [
            {"title": "UAV-based multi-view imagery for precision agriculture", "content": "Utilizing DJI M30T for phenotypic data extraction at different flight heights..."},
            {"title": "Enhanced HRNet for semantic segmentation", "content": "Introducing Adaptive Fusion Enhancement Module (AFEM) and Convolutional Shift Attention Module (CSAM)..."},
            {"title": "Crop yield prediction combining ERA5 climate variables", "content": "Regression tasks utilizing panel data and historical temperature/humidity..."}
        ]